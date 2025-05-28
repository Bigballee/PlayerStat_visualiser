import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_career_by_club(player_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find("table", class_="items")
    if not table:
        print("⚠️ Career table not found.")
        return

    rows = table.find_all("tr", class_=["odd", "even"])

    data = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 8:
            continue

        # Extract club name cleanly
        club_cell = cols[2]
        club_img = club_cell.find("img")
        if club_img and club_img.has_attr("alt"):
            club = club_img["alt"]
        else:
            club = club_cell.text.strip()

        appearances = cols[4].text.strip().replace("-", "0")
        goals = cols[6].text.strip().replace("-", "0")
        assists = cols[7].text.strip().replace("-", "0")

        try:
            data.append({
                "Club": club,
                "Appearances": int(appearances),
                "Goals": int(goals),
                "Assists": int(assists)
            })
        except ValueError:
            continue  # skip rows with non-numeric data

    df = pd.DataFrame(data)
    summary = df.groupby("Club", as_index=False).sum()

    print("\n📊 Career Summary by Club:\n")
    print(summary.to_string(index=False))

    
# Use correct URL with stat breakdown
fetch_career_by_club("https://www.transfermarkt.com/samuel-etoo/leistungsdaten/spieler/4257")
