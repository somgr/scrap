import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

data = soup.find('div', class_='col-lg-4 col-md-6 mb-4')

name = data.find('h4', class_='card-title').text.replace('\n', '')
price = data.find('h5').text
url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
