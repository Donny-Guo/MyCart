import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the IMDb Top 250 page
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the movie data
table = soup.find('table', class_='chart full-width')

# Open a CSV file to write the scraped data
with open('imdb_top250.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Rank', 'Title', 'Year', 'Rating'])  # Write header row
    
    # Iterate over the rows of the table, excluding the header row
    rows = table.find_all('tr')
    for row in rows[1:]:
        try:
            # Get the movie rank
            rank = row.find('td', class_='titleColumn').text.strip().split('.')[0]

            # Get the movie title
            title = row.find('td', class_='titleColumn').find('a').text.strip()

            # Get the movie year
            year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').text.strip('()')

            # Get the movie rating
            rating = row.find('td', class_='imdbRating').find('strong').text.strip()

            writer.writerow([rank, title, year, rating])  # Write data row

        except AttributeError as e:
            print(f'Skipping row: {e}')  # Print error message for missing elements
            continue

print("Scraping complete. Data saved to 'imdb_top250.csv'")
