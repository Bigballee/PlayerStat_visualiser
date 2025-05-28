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

        club = cols[2].img['alt'] if cols[2].img else cols[2].text.strip()
        appearances = cols[4].text.strip().replace("-", "0")
        goals = cols[6].text.strip().replace("-", "0")
        assists = cols[7].text.strip().replace("-", "0")

        data.append({
            "Club": club,
            "Appearances": int(appearances),
            "Goals": int(goals),
            "Assists": int(assists)
        })

    # Use pandas to group and sum by club
    df = pd.DataFrame(data)
    summary = df.groupby("Club", as_index=False).sum()

    # Print it out
    print("\n📊 Career Summary by Club:\n")
    print(summary.to_string(index=False))
    
    
# ✅ Use correct URL with stat breakdown
fetch_career_by_club("https://www.transfermarkt.com/samuel-etoo/leistungsdaten/spieler/4257")
