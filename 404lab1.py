import requests

print(requests.__version__)

requests.get("https://www.google.com")

var = requests.get("https://raw.githubusercontent.com/DevinDai13/CMPUT-404/Lab1/404lab1.py")

print(var.content)

