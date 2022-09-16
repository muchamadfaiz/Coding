# Parsing website with handling error
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

# membuka url
try:
    url = "http://olympuss.realpython.org/profiles/dionysus"
    urlhandle = urlopen(url)
except HTTPError as e:
    print(e)
else:
# proses scrapping
    soup = BeautifulSoup(urlhandle,"html.parser")
    print(soup.head)
