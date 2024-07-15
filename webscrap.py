import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the webpage
url = 'http://example.com/tablepage'
response = requests.get(url)
webpage_content = response.text

# Step 2: Parse the HTML
soup = BeautifulSoup(webpage_content, 'html.parser')
data = []

# Step 3: Extract the table
table = soup.find('table')

# Step 4: Extract headers
headers = [header.text for header in table.find_all('th')]

# Step 5: Extract rows
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    data.append([cell.text for cell in cells])

# Step 6: Save data to CSV
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Header
    for row in data:
        writer.writerow(row)