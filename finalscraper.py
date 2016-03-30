__author__ = 'dbortmas'

import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://jobs.code4lib.org'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('div', attrs={'class': 'row'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./C4LjobScraper.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Date", "Job", "Skills", "FT/PT"])
writer.writerows(list_of_rows)