import http
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    url = "http://olympusssss.realpython.org/profiles/dionysus"
except HTTPError as e:
    print(e)
except URLError as f:
    print(f"{f} URL not found bro")
finally:
    print("its worked bro!!")

# page = urlopen(url)
# # print(page)
# # html_bytes = page.read()
# # html = html_bytes.decode("utf-8")
# soup = BeautifulSoup(page, "html.parser")
# print(soup)


