import requests
from bs4 import BeautifulSoup

def inspect_trophy_table(player_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    section = soup.find('div', class_="erfolg")
    if not section:
        print("⚠️ Trophy section not found.")
        return

    print("📊 Trophy Table Structure:\n")

    boxes = section.find_all('div', class_="box")

    for box in boxes:
        title = box.find("div", class_="header").text.strip()
        print(f"🏆 {title}")

        rows = box.find_all("tr", class_=["odd", "even"])
        for row in rows:
            cols = row.find_all("td")
            print("  Row:")
            for i, col in enumerate(cols):
                print(f"    Index {i}: '{col.text.strip()}'")
            print("-" * 30)
        print("=" * 40)

# Test on Eto’o
inspect_trophy_table("https://www.transfermarkt.com/samuel-etoo/erfolge/spieler/4257")
