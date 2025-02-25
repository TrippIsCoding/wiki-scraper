import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
response = requests.get(url)

if response.status_code == 200:
    print("Page fetched!")
    soup = BeautifulSoup(response.text, "html.parser")
else:
    print(f"Failed to fetch page: {response.status_code}")
    exit()

table = soup.find("table", {"class": "wikitable"})
if not table:
    print('Table not found!')
    exit()

rows = table.find_all("tr")[2:]

data = []
for row in rows:
    cols = row.find_all("td")
    place = cols[0].text.strip()
    population = cols[2].text.strip().replace(",", "")
    data.append([place, population])

print(f"Scraped {len(data)} countries and territories!")

with open('places.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(['Places', 'Population'])
    writer.writerows(data)

print('Data saved to places.csv!')