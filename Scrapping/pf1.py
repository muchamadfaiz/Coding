from bs4 import BeautifulSoup
from urllib.request import urlopen
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam"
fhandle = urlopen(url)
print(type(fhandle))

soup = BeautifulSoup(fhandle,"html.parser")
lists = soup.find_all("section", class_="listing-search-item")

number = 0
with open("housing.csv", "w", encoding="utf8", newline="") as f:
    thewriter = writer(f)
    header = ["Number","Title", "Location", "Price", "Area"]
    thewriter.writerow(header)
    for i in lists:
        number += 1
        title = i.find("a", class_="listing-search-item__link--title").text.strip()
        location = i.find("div", class_="listing-search-item__sub-title").text.strip()
        price = i.find("div", class_="listing-search-item__price").text.strip()
        living_area = i.find("li", class_="illustrated-features__item illustrated-features__item--surface-area").text.strip()
        
        newlist = [number, title, location, price, living_area]
        thewriter.writerow(newlist)
print("finish")

   