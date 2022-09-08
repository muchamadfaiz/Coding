import urllib.request
import xml.etree.ElementTree as ET

base_url = "http://py4e-data.dr-chuck.net/comments_1642965.xml"
data = urllib.request.urlopen(base_url)
string = data.read().decode('utf-8')
# print(type(string))
# print(string)
commentinfo = ET.fromstring(string)
pertama = commentinfo.findall("comments/comment")
sum = 0
for item in pertama:
    count = int(item.find("count").text)
    sum += count
print(sum)

# result = tree.findall("comment")
# print(result)