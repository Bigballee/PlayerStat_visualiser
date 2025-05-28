import requests
from bs4 import BeautifulSoup
import json 

def inspect_trophy_table(player_url,output_filename):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    trophy_data = []

    # Find all trophy group headers and the tables below them
    headings = soup.find_all("h2")
    for heading in headings:
        title = heading.text.strip()
        table = heading.find_next("table", class_="auflistung")
        if not table:
            continue

        print(f"\n🏆 {title}")
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                year = cols[0].text.strip()
                club = cols[2].text.strip() if len(cols) > 2 else "N/A"
                print(f"  📅 {year} - 🏟️ {club}")
                trophy_data.append({
                    "Title": title,
                    "Year": year,
                    "Club": club
                })
                
        print("-" * 40)

    # Save to JSON
    with open(output_filename, "w") as f:
        json.dump(trophy_data, f, indent=2)

    print(f"✅ Exported to {output_filename}")

# Test on Eto’o
inspect_trophy_table("https://www.transfermarkt.com/samuel-etoo/erfolge/spieler/4257", "etoo_trophies.json")
