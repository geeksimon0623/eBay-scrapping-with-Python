import requests
from bs4 import BeautifulSoup
import csv

def get_page(url):
    response = requests.get(url)
    if not response.ok :
        print('server not responding')
    else:
        soup = BeautifulSoup(response.text,'lxml')
    return soup

def get_details(soup):
    try:
        title = soup.find('span',class_='B_NuCI').get_text()
    except:
        title = ' '

    try:
        price = soup.find(class_='_30jeq3').string
    except:
        price = ' '

    try:
        rating = soup.find(class_='_3uSWvT').text
    except:
        rating = ' '

    data = {
        'title':title,
        'price':price,
        'rating':rating
    }
    return data



def get_links(soup):
    try:
        links = soup.find_all('a',class_='IRpwTa')
    except:
        links = []

    urls = ['https://www.flipkart.com' + item.get('href') for item in links]
    return urls

def write_csv(data):
    with open('flip.csv','a',encoding='utf8') as f:
        writer = csv.writer(f)
        row = data['title'],data['price'],data['rating']
        writer.writerow(row)
    
        

def main():
    url = 'https://www.flipkart.com/search?q=watches+men&sid=r18%2Cf13&as=on&as-backfill=on&page=2'

    products = get_links(get_page(url))
    
    for link in products:
        data = get_details(get_page(link))
        write_csv(data)


if __name__ == '__main__':
    main()