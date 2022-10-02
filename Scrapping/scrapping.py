import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception (f"Unable to download the page {url}")
    page_content = response.text
    soup = BeautifulSoup(page_content, "html.parser")

    return soup


def extract_data(soup):
    tags =soup.find_all("section")

    data_list = []
    for tag in tags:
        name = tag.find("a",class_= "listing-search-item__link listing-search-item__link--title").text.strip()
        address = tag.find("div",class_= "listing-search-item__sub-title").text.strip()
        price = tag.find("div",class_= "listing-search-item__price").text.strip()
        area = tag.find("li",class_= "illustrated-features__item illustrated-features__item--surface-area").text.strip()
    
        # sorting data
        data_dict = {
            "name" : name,
            "address" : address,
            "price" : price,
            "area" : area
        }
        data_list.append(data_dict)

    return data_list


def display_data(tags):
    count = 0
    for i in tags:
        count += 1
        print("---------------------------")
        print(f"hotel = {count}")
        print(f"Hotel Name = {i['name']}")
        print(f"Hotel Adress = {i['address']}")
        print(f"Hotel Price = {i['price']}")
        print(f"Hotel Area = {i['area']}")
    

# putting all together
def scrape_data():
    page = get_page("https://www.pararius.com/apartments/amsterdam")
    data = extract_data(page)
    display_data(data)

scrape_data()






