from cmath import log
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.msmemart.com/msme/listings/company-list/advertising-materials/90/1297/Supplier"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

companies = []  # a list to store quotes

li = soup.find('ul', attrs={'class': 'upl_list'})

print(li)

index = 0

for row in li.findAll('li'):
    index += 1
    company = {}
    company['Sr.No.'] = index
    company['Name'] = row.div.div.h4.a.text  # row.a['href']
    # company['Products/Services'] = row.img['src']
    # company['Website(If available)'] = row.img['alt'].split(" #")[0]
    # company['Address'] = row.img['alt'].split(" #")[1]
    # company['Contact No.'] = row.img['alt'].split(" #")[1]

    companies.append(company)

filename = 'companies.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['Sr.No.', 'Name', 'Products/Services',
                       'Website(If available)', 'Address', 'Contact No.'])
    w.writeheader()
    for company in companies:
        w.writerow(company)
