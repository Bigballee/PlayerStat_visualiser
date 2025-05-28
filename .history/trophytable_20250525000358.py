import requests
from bs4 import BeautifulSoup

def inspect_trophy_table(player_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find("table", class_="auflistung")
    if not table:
        print("⚠️ Could not find trophy table.")
        return

    rows = table.find_all("tr")

    print("📊 Trophy Table Structure:\n")

    for row in rows:
        cols = row.find_all("td")
        if not cols:
            continue

        print("  Row:")
        for i, col in enumerate(cols):
            print(f"    Index {i}: '{col.text.strip()}'")
        print("-" * 30)


# Test on Eto’o
inspect_trophy_table("https://www.transfermarkt.com/samuel-etoo/erfolge/spieler/4257")
