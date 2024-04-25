
import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_companies_traded_on_the_JSE"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables on the page
tables = soup.find_all("table")

# Print each table
for index, table in enumerate(tables, 1):
    print(f"Table {index}:")
    print(table)
    print("\n\n")
