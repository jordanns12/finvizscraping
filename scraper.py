from bs4 import BeautifulSoup
import requests as re

url = "https://finviz.com/groups.ashx"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
          'Upgrade-Insecure-Requests': '1', 'Cookie': 'v2=1495343816.182.19.234.142', 'Accept-Encoding': 'gzip, deflate, sdch',
           'Referer': "http://finviz.com/groups.ashx"}

response = re.get(url, headers=headers)

if response.status_code == 200:
    print("Request successful")
else:
    print(f"Request failed with status code: {response.status_code}")

soup = BeautifulSoup(response.content, 'html.parser')

sector_container  = soup.find('div', class_='futures pt-2.5')
print(soup)
# Extract sector names and percent changes
# sectors = []
# percent_changes = []

# for div in sector_container.find_all('div', class_='futures pt-2.5'):
#     sector = div.find('div', class_='label').text
#     change = div.find('div', class_='value').text
#     sectors.append(sector)
#     percent_changes.append(change)

# # Print sectors with their percent changes
# for sector, change in zip(sectors, percent_changes):
#     print(f"{sector}: {change}")