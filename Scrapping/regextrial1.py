from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<TITLE >(.*)</title  / >"
title = re.findall(pattern, html)
print(title)