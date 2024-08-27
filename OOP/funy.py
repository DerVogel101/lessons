import urllib.request

path = "https://raw.githubusercontent.com/DerVogel101/funny-py-lib/master/muple.py"
Muple: "Muple"
exec(urllib.request.urlopen(path).read().decode())
