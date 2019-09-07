from bs4 import BeautifulSoup
import os
import sys

if __name__ == '__main__':
    f = open("sitemap.xml", "r")
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('loc')
    for link in links:
        os.system("wget -k -p "+link.contents[0])
