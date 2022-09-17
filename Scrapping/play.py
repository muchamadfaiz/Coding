from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"
fhandle = urlopen(url)

soup = BeautifulSoup(fhandle, "html.parser")
# print(soup.prettify)

# name_list = soup.findAll("span", {"class":"green"})
# for name in name_list:
#     print(name.text)

# name = soup.find(id="giftList")
# print(name)

name = soup.find("table",{"id":"giftList"}).tr.next_siblings
for sibling in name:
    print(sibling)

