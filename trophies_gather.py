import requests
from bs4 import BeautifulSoup
import json

def scrape_trophies(player_url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    section = soup.find('div', class_="erfolg")
    if not section:
        print("⚠️ Trophy section not found.")
        return

    trophy_table = section.find_all('div', class_="box")

    trophies = []

    for box in trophy_table:
        title = box.find("div", class_="header").text.strip()

        rows = box.find_all("tr", class_=["odd", "even"])
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                competition = cols[0].text.strip()
                count = cols[1].text.strip()
                years = cols[2].text.strip()
                trophies.append({
                    "Title": title,
                    "Competition": competition,
                    "Count": count,
                    "Years": years
                })

    # Save to JSON
    with open(filename, "w") as f:
        json.dump(trophies, f, indent=2)
    print(f"✅ Exported to {filename}")

# Run for Eto'o
scrape_trophies("https://www.transfermarkt.com/samuel-etoo/erfolge/spieler/4257", "etoo_trophies.json")

# Run for Drogba
scrape_trophies("https://www.transfermarkt.com/didier-drogba/erfolge/spieler/3924", "drogba_trophies.json")
