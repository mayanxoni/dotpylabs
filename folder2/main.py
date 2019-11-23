import requests
from bs4 import BeautifulSoup

req = requests.get('http://bewakoof.com/desi-collection/')

# for printing status code of the request
# print(req.status_code)

# for printing source code of the webpage
# print(req.content)

soup  = BeautifulSoup(req.content, 'html.parser')

# for making the content beautiful
# print(soup.prettify())

# for opening a CSV file in write mode
fp = open('web.csv', 'w')
fp.write('t-shirt name , price , image\n')


for products in soup.find_all('div' , {'class' : 'productCardBox'} ):
    for img in products.find_all('div', {'class' : 'productCardImg'}):
        print(detail.find_all('img'))
        fp.write('\n')
    for detail in products.find_all('div', {'class' : 'productCardDetail'}):
        print(detail.find_all('h3'))
        fp.write(str(detail.find_all('h3')[0].text))
        fp.write(',')
        fp.write(str(detail.find_all('b')[1].text))
        fp.write(',')
    #     break
    # break
