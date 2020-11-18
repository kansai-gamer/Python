import urllib.request

url = "https://raw.githubusercontent.com/murayama333/python2020/master/02_oop/text/README.md"

req = urllib.request.Request(url)

resp = urllib.request.urlopen(req)

body = resp.read()

html = body.decode("UTF-8")

rows = html.split("\n")

for row in rows:
    if "str" in row:
        print(row)