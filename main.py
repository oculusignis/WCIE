import requests

url = "http://meteolakes.ch/api/coordinates/534700/144950/geneva/temperature/1537034400000/1537768800000/20"
r = requests.get(url)

print(r.content)
