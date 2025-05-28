import requests
from bs4 import BeautifulSoup
import pandas as pd



# Function to gather player data from Transfermarkt
def gather_transfermarktdata(player_url):
    # pretends to be a browser 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    #download the page from the URL
    response = requests.get(player_url, headers=headers)
    
    #turns the html into a format where we can search and extract data
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing player data
    table = soup.find('table', class_='items')
    if not table:
        print("⚠️ Could not find career table on page.")
        return pd.DataFrame()  # Return empty table
    
    
    #rows = table.find_all('tr', class_=['odd', 'even']) 
    
    #loops over each row in the table 
    #stores the results of each row in our dataframe
    data = []
    
    #for row in rows:
     #gets all table columns   
       # cols = row.find_all('td')
       for row in rows:
        cols = row.find_all('td')
    print([col.text.strip() for col in cols])  # See what data you're getting
    break  # Just print the first row for inspection

        
        #if there are more than 7 columns, we skip the row
        if len(cols) > 7: 
            continue
        
    #pull data from each season of the player    
    #each column holds information about the player
    # text.strip() removes any extra spaces
        season = cols[0].text.strip()
        club = cols[3].img['alt'] if cols[3].img else cols[3].text.strip()
        appearances = cols[4].text.strip()
        goals = cols[5].text.strip()
        assists = cols[6].text.strip()
        
        # stores the data in a dictionary
        data.append({
            'Season': season,
            'Club': club,
            'Appearances': appearances,
            'Goals': goals,
            'Assists': assists
        })
        
        
        # Create a DataFrame from the data
    return pd.DataFrame(data)
    
etoo_data = gather_transfermarktdata("https://www.transfermarkt.com/samuel-etoo/leistungsdatendetails/spieler/4257")
drogba_data = gather_transfermarktdata("https://www.transfermarkt.com/didier-drogba/leistungsdatendetails/spieler/3924")
   
   # this function runs gather_transfermarktdata for both players 
print("Eto'0 Career:")
print(etoo_data.head())
    
print("\nDrogba Career:")
print(drogba_data.head())


