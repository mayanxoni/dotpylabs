import requests
from bs4 import BeautifulSoup

req = requests.get('http://bewakoof.com/desi-collection/')

# for printing status code of the request
# print(req.status_code)

# for printing source code of the webpage
# print(req.content)

soup  = BeautifulSoup(req.content, 'html.parser')

# for making the content beautiful
print(soup.prettify())
fp = open('web.csv', 'w')


for products in soup.find_all('div' , {'class' : 'productCardBox'} ):
    for detail in products.find_all('div', {'class' : 'productCardDetail'}):
        print(detail.find_all('b'))
        fp.write(str(detail.find_all('b')[0].text))
        fp.write(',')
        fp.write(str(detail.find_all('b')[1].text))
        break
    break
