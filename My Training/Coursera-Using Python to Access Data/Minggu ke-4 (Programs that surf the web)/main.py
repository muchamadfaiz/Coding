from urllib import request
from bs4 import BeautifulSoup

# 1
base_url = "http://py4e-data.dr-chuck.net/known_by_Malachai.html"
resp = request.urlopen(base_url)
html = resp.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
x = []
for tag in tags:
    c = tag.get('href', None)
    x.append(c)
y = x[17]
print ("Retrieving: " + y)

# 2
resp = request.urlopen(y)
html = resp.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
x = []
for tag in tags:
    c = tag.get('href', None)
    x.append(c)
y = x[17]
print ("Retrieving: " + y)

# 3
resp = request.urlopen(y)
html = resp.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
x = []
for tag in tags:
    c = tag.get('href', None)
    x.append(c)
y = x[17]
print ("Retrieving: " + y)

# 4
resp = request.urlopen(y)
html = resp.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
x = []
for tag in tags:
    c = tag.get('href', None)
    x.append(c)
y = x[17]
print ("Retrieving: " + y)

# 5
resp = request.urlopen(y)
html = resp.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
x = []
for tag in tags:
    c = tag.get('href', None)
    x.append(c)
y = x[17]
print ("Retrieving: " + y)

# 6
resp = request.urlopen(y)
html = resp.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
x = []
for tag in tags:
    c = tag.get('href', None)
    x.append(c)
y = x[17]
print ("Retrieving: " + y)

# 7
resp = request.urlopen(y)
html = resp.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
x = []
for tag in tags:
    c = tag.get('href', None)
    x.append(c)
y = x[17]
print ("Retrieving: " + y)

# # 8
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 9
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)
# # 10
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 11
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 12
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 13
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 14
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 15
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 16
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 17
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)

# # 18
# resp = request.urlopen(y)
# html = resp.read()
# soup = BeautifulSoup(html, "html.parser")
# tags = soup('a')
# x = []
# for tag in tags:
#     c = tag.get('href', None)
#     x.append(c)
# y = x[2]
# print ("Retrieving: " + y)


