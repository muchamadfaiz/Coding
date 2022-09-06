from urllib import request
from bs4 import BeautifulSoup

# 1

base_url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
count = 4
base = []
for scrape in range(count):
    resp = request.urlopen(base_url).read()
    soup = BeautifulSoup(resp, "html.parser")
    tags = soup('a')

    x = []
    for tag in tags:
        c = tag.get('href', None)
        x.append(c)
    y = x[2]
    print ("Retrieving: " + y)

# count = 4
# data = ["pawpaw", "umiw", 23, True]
# for x in range(count):
#     print (data)

