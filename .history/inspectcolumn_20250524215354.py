import requests
from bs4 import BeautifulSoup

def inspect_transfermarkt_row(player_url):
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

    # Print the first row only
     print("🧱 First 5 Rows:")
    for idx, row in enumerate(rows[:5]):  # Loop over first 5 rows only
        cols = row.find_all('td')
        print(f"\nRow {idx + 1}:")
        for i, col in enumerate(cols):
            print(f"  Index {i}: {col.text.strip()}")

# ✅ Use correct URL with stat breakdown
inspect_transfermarkt_row("https://www.transfermarkt.com/samuel-etoo/leistungsdatendetails/spieler/4257")
