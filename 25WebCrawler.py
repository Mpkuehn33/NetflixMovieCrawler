import requests
from bs4 import BeautifulSoup

def redditSpider():
    URL = 'http://uk.netflixable.com/2016/09/complete-alphabetical-list-sat-oct-1.html'
    source = requests.get(URL)
    Soup = BeautifulSoup(source.text, "html.parser")
    fw = open('movies.txt', 'w')
    for link in Soup.findAll('b'):
        fw.write(str(link.encode('utf-8')))
        fw.write('linebrk')

    fw.close()
redditSpider()

