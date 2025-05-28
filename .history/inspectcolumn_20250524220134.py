import requests
from bs4 import BeautifulSoup

def inspect_transfermarkt_rows(player_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='items')
    if not table:
        print("⚠️ Could not find career table on page.")
        return

    rows = table.find_all('tr', class_=['odd', 'even'])

    print("🔎 Debugging season column values:\n")

    for row in rows:
        cols = row.find_all('td')
        if not cols or len(cols) < 1:
            continue

        season = cols[0].text.strip()
        print(f"Found season column value: '{season}'")  # 👈 ADD THIS

        # Now try showing only those with a slash like "04/05"
        if "/" in season:
            print(f"\n📌 Season: {season}")
            for i, col in enumerate(cols):
                print(f"  Index {i}: {col.text.strip()}")

        # Stop after first 10 season-like rows
        if season.startswith("98") or season.startswith("17"):
            break



# ✅ Use correct URL with stat breakdown
inspect_transfermarkt_row("https://www.transfermarkt.com/samuel-etoo/leistungsdatendetails/spieler/4257")
