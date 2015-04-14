import urllib.request
import urllib.parse

try:
    x = urllib.request.urlopen("https://www.google.pl/search?q=test")
    print(x.read())
except Exception as e:
    print(str(e))

try:
    url = "https://www.google.pl/search?q=test"
    headers = {}
    headers["user-agent"] = "noob programmer"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open("d:\\headers.txt", "w")
    saveFile.writelines(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))

"""
url = "http://pythonprogramming.net/"
v = {
    "s":"baisic",
    "submint":"search"
    }
print("or:", v)
data = urllib.parse.urlencode(v)
print("urlencode:", data)
data = data.encode('utf-8')
print("d.encode:", data)
req = urllib.request.Request(url, data)
print("req:", req)
resp = urllib.request.urlopen(req)
print("resp req:", resp)
respData = resp.read()

print("respdata:", respData)"""