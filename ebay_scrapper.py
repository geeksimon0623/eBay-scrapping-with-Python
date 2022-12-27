import requests
from bs4 import BeautifulSoup
import csv


def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('server is not responding')
    else :
        soup = BeautifulSoup(response.text,'lxml')
        return soup

def get_details(soup):
    try:
        title = soup.find('h1').get_text().replace('Details about  \xa0',' ')
    except:
        title = ''

    try:
        price = soup.find('span',id='prcIsum').get_text().split()[1]
    except:
        price = ''

    try:
        sold = soup.find('span',class_='vi-qtyS-hot-red').find('a').get_text().split()[0]
        print(sold)
    except:
        sold = ''

    data = {
        'title':title,
        'price':price,
        'sold':sold
    }
    return data


def get_index_data(soup):
    try:
        links = soup.find_all('a',class_='s-item__link')
    except:
        links = []
    
    urls = [item.get('href') for item in links]
    return urls


def write_csv(data):
    with open('output.csv','a') as f:
        writer = csv.writer(f)

        try:
            row = data['title'],data['price'],data['sold']
            writer.writerow(row)
        except:
            pass

    
def main():
    url = 'https://www.ebay.com/sch/i.html?_nkw=men%27s+watches&_pgn=1'
    products = get_index_data(get_page(url))
    
    for link in products:
        data = get_details(get_page(link))
        write_csv(data)


if __name__ == '__main__':
    main()