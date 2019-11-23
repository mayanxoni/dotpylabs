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