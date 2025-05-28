import requests
from bs4 import BeautifulSoup

def show_transfermarkt_table_structure(player_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the performance overview table
    table = soup.find("table", class_="items")
    if not table:
        print("⚠️ Could not find table.")
        return

    rows = table.find_all("tr", class_=["odd", "even"])
    print("📊 Sample Row Column Layout:\n")

    # Just show the first non-empty row to explain structure
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 0:
            continue

        for i, col in enumerate(cols):
            raw_text = col.text.strip()
            print(f"Index {i}: '{raw_text}'")
        break  # only show first row

# Example: Samuel Eto'o career overview page
show_transfermarkt_table_structure("https://www.transfermarkt.com/samuel-etoo/leistungsdaten/spieler/4257")
