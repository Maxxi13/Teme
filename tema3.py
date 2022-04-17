import requests
import csv
from bs4 import BeautifulSoup
from csv import writer

URL = 'https://frsah.ro/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#lists = soup.find(class_='wptb-preview-table wptb-element-main-table_setting-18262')

#rows = soup.find_all('tr', class_='wptb-row')
cells = soup.find_all('td', class_='wptb-cell')

with open('turnee.csv', 'w', encoding='utf8', newline='') as csvfile:
    thewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for cell in cells:
     thewriter.writerow([cell.text])



with open('turnee.csv', 'r') as csv_file:
     rows = csv.reader(csv_file, delimiter = ',')
     for row in rows:
          print(row)



new_lines = [['Dacia', 'Logan', 2005, 75],['Renault', 'Clio', 2005, 75]]
with open('turnee.csv', 'r+', newline='', encoding='utf-8') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=',')
     for new_line in new_lines:
         csv_writer.writerow(new_line)
