# Parse website data using regular expression (regex)
"""
Real-world HTML can be much more complicated and 
far less predictable than the HTML on the Aphrodite profile page. 
Here’s another profile page with some messier HTML that you can scrape
"""
# 1. call module request on urllib (library) and import urlopen (function)
from urllib.request import urlopen

# 2. call module "re" for activating regular expression
import re

# 3. make variable named "url" to store a string of url web page
url = 'http://olympus.realpython.org/profiles/poseidon'

# 4. to open a remote object across a network (can read HTML, files, images, etc)
# and it will return a HTTPResponse object -> output = http.client.HTTPResponse object at 0x00000289E3003340
page = urlopen(url) 

# 5. to extract HTML from the page -> return sequence of bytes
html_bytes = page.read() 

# 6. to decode the bytes to a string using (UTF-8) --> for reading in terminal python
html = html_bytes.decode("utf-8") # decode the bytes to a string using (UTF-8)
# print(type(html))
print(html)

# Extract Text wtihin tag <title> from HTML with regex --> we cant use string method in previous ex.

# 1. make a pattern using regex
pattern = "<title.*>(.*)</title.*>"

# 2. use re.findall(pattern, string) to search the pattern on the string
title = re.findall(pattern, html)
# print(title) # --> [Profile: Poseidon]

# 3. and you can substitute/replace the word with re.sub()
sub = re.sub("<.*>","pawpaw",html) #substitute anyword inside <> with greedy method
# print(sub)

# 4. and you can substitute/replace the word with re.sub()
sub = re.sub("<.*?>","pawpaw",html) #substitute anyword inside <> with non-greedy method
# print(sub)

