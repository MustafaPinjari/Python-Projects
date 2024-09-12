from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests as rq
import os
from bs4 import BeautifulSoup
import time

path = input("Enter the path to ChromeDriver (e.g., C:/path/to/chromedriver.exe): ")
url = input("Enter the URL: ")
output = "output"

def get_url(path, url):
    # Create a Service object to handle the ChromeDriver path
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    print("Loading...")

    # Get the page's full HTML
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()  # Close the browser when done
    return res

def get_img_links(res):
    soup = BeautifulSoup(res, "lxml")
    imglinks = soup.find_all("img", src=True)
    return imglinks

def download_img(img_link, index):
    try:
        extensions = [".jpeg", ".jpg", ".png", ".gif"]
        extension = ".jpg"

        for exe in extensions:
            if img_link.find(exe) > 0:
                extension = exe
                break

        img_data = rq.get(img_link).content
        with open(output + "\\" + str(index) + extension, "wb+") as f:
            f.write(img_data)
    except Exception as e:
        print(f"Failed to download image {index}: {e}")

result = get_url(path, url)
time.sleep(60)
img_links = get_img_links(result)

# Create the output directory if it doesn't exist
if not os.path.isdir(output):
    os.mkdir(output)

# Download each image
for index, img_link in enumerate(img_links):
    img_link = img_link["src"]
    print(f"Downloading image {index + 1}...")

    if img_link:
        download_img(img_link, index)

print("Download Complete!!!")
