import requests
from bs4 import BeautifulSoup


def show_transfermarkt_competition_data(player_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find("table", class_="items")
    if not table:
        print("⚠️ Could not find career overview table.")
        return

    rows = table.find_all("tr", class_=["odd", "even"])

    print("📊 Appearances, Goals, and Assists by Competition:\n")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        competition = cols[1].text.strip()
        appearances = cols[2].text.strip().replace("-", "0")
        goals = cols[3].text.strip().replace("-", "0")
        assists = cols[4].text.strip().replace("-", "0")

        print(f"🏆 {competition}\n  👕 Appearances: {appearances}\n  ⚽ Goals: {goals}\n  🎯 Assists: {assists}\n")

# Example: Samuel Eto'o career overview page
show_transfermarkt_competition_data("https://www.transfermarkt.com/samuel-etoo/leistungsdaten/spieler/4257")
