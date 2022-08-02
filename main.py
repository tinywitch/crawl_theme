from bs4 import BeautifulSoup
import os
import sys

if __name__ == '__main__':
    f = open("sitemap.xml", "r")
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('loc')
    for link in links:
        os.system("wget --user-agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -k -p "+link.contents[0])

        