# import requests
# from bs4 import BeautifulSoup
# import csv

# key = "hotels"
# location = "london"
# url = "https://www.yell.com/ucs/UcsSearchAction.do?keywords={}&location={}&scrambleSeed=86061706&pageNum=".format(key, location)
# # headers = {
# # ""
# # }
# req = requests.get(url)
# print(req)


import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code