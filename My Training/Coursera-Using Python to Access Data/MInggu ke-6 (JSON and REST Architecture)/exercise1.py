from encodings import utf_8
import json
import urllib.request

# sample data
# base_url = "https://py4e-data.dr-chuck.net/comments_42.json"
# actual data
base_url = "http://py4e-data.dr-chuck.net/comments_1642966.json"
response = urllib.request.urlopen(base_url)
html = response.read()

info = json.loads(html)
print("user count : {}".format(len(info["comments"])))
comments = info["comments"]
sum = 0
for angka in comments:
    b = angka["count"]
    sum += b
    print("user {} angka {}".format(angka["name"], angka["count"]))
    # print(f"user {angka['name']} angka {angka['count']}")
    # print("user", angka["name"], "angka", angka["count"])
print(f"total semua {sum}")
