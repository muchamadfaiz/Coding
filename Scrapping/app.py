# Parse website data using string methods

# 1. call module request on urllib (library) and import urlopen (function)
from urllib.request import urlopen

# 2. make variable named "url" to store a string of url web page
url = 'http://olympus.realpython.org/profiles/aphrodite'

# 3. to open a remote object across a network (can read HTML, files, images, etc)
# and it will return a HTTPResponse object -> output = http.client.HTTPResponse object at 0x00000289E3003340
page = urlopen(url) 

# 4. to extract HTML from the page -> return sequence of bytes
html_bytes = page.read() 

# 5. to decode the bytes to a string using (UTF-8) --> for reading in terminal python
html = html_bytes.decode("utf-8") # decode the bytes to a string using (UTF-8)
# print(type(html))
print(html)

# Extract Text wtihin tag <title> from HTML with string method --> we can use string slicing

# 1. get the index of string "<title>" using find() fun.
title_index = html.find("<title>")
print(title_index)

# 2. get the index of the first letter in the "<title>" 
start_index = title_index + len("<title>")
print(start_index)

# 3. get the index of the closing tag </title> using find() fun.
closing_index = html.find("</title>")
print(closing_index)

# 4. extract the title with slicing
title = html[start_index:closing_index]
print(title)

# string = "pawpaw makan nasi"
# pawpaw = string.find("makan")
# print(pawpaw)