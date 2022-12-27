import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
r = requests.get(url)
htmlcontent = r.content


# step-2 parse the html
soup = BeautifulSoup(htmlcontent,'html.parser')

# step-3 html tree traversal
title = soup.title
# print(title.string)

# commp=ny used objects
#  1.tag
#  2.navigable string
#  3.beauiful soup
#  4.comment

paras = soup.find_all('p')

# print(soup.find('p')) only find first paragraph
#  print(soup.find('p')['class'])  gives classes names

# to find elements with class lead
# print(soup.find_all("p",class_="lead"))


# Get the text from the elements
# print(soup.find('p').get_text())

# To get all the links from a web page
# anchors = soup.find_all('a')
# all_links = set()
# for link in anchors:
#     if (link.get('href') != '#'):
#         print('http://codewithharry.com'+link.get('href'))


# getting a div from id
navbarsupportcontent = soup.find(id='navbarSupportedContent')
# print(navbarsupportcontent)
# print(navbarsupportcontent.parent)


# selecting from id
elem = soup.select('#loginModal')
print(elem)

