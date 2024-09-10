import requests as rq
from bs4 import BeautifulSoup
import os

url = input("Enter URL: ")
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)

soup = BeautifulSoup(data.text, "html.parser")

links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Path to save the fetched links
save_path = r'path dalo jaha file save kari ho complet absolute path'

# Mode selection for overwriting or appending to the file
mode = input("Enter 'w' to overwrite the file, 'a' to append: ").lower()

with open(save_path, mode) as saved:
    print(links[:10], file=saved)
    
print(f"Links have been saved to {save_path}")
