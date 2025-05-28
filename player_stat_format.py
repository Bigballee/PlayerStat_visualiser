import requests
from bs4 import BeautifulSoup
import json


def show_transfermarkt_competition_data(player_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(player_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find("table", class_="items")
    if not table:
        print(" Could not find career overview table.")
        return

    rows = table.find_all("tr", class_=["odd", "even"])

    print(" ⚽️ Drogba Stats per Competiton:\n")


    data = []
    
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        competition = cols[1].text.strip()
        appearances = cols[2].text.strip().replace("-", "0")
        goals = cols[3].text.strip().replace("-", "0")
        assists = cols[4].text.strip().replace("-", "0")

        print(f"🏆 {competition}\n  👕 Appearances: {appearances}\n  ⚽ Goals: {goals}\n  🎯 Assists: {assists}\n")
        
        data.append({
            "Competition": competition,
            "Appearances": int(appearances),
            "Goals": int(goals),
            "Assists": int(assists)
        })

    # Export to JSON
    with open("drogba_stats.json", "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Exported to drogba_stats.json")    
        
        
        
        
        

# Example: Player career overview page
show_transfermarkt_competition_data("https://www.transfermarkt.co.uk/didier-drogba/leistungsdaten/spieler/3924")
