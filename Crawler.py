import sys
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

valid_start = False
valid_goal = False
if len(sys.argv) > 1:
    URL_start = str(sys.argv[1])
    if urlparse(URL_start).scheme == 'https':
        if '/wiki/' in URL_start:
            valid_start = True
    if len(sys.argv) == 3:
        URL_goal = str(sys.argv[2])
        if urlparse(URL_goal).scheme == 'https':
            if '/wiki/' in URL_goal:
                valid_goal = True
if not valid_start:
    URL_start = "https://en.wikipedia.org/wiki/Special:Random"
if not valid_goal:
    URL_goal = "https://en.wikipedia.org/wiki/Philosophy"

print("\n\n\nStarting URL is: " + URL_start)
print("Goal URL is: " + URL_goal + "\n\n\n")
response = requests.get(URL_start)
html = response.text

article_chain = []

soup = BeautifulSoup(html, 'html.parser')
print("Starting Page: " + soup.title.string)
target_url = "https://en.wikipedia.org" + soup.find(id = 'mw-content-text').p.a.get('href')

#Checks if crawler is looping, if page has no links,  or Philosophy has been found
def continue_crawl(search_history, target_url):
    if target_url in search_history:
        print("\n\nCrawler is looping. \n" + target_url + " has previously been visited\n\n")
        print("Crawler history: ")
        print(*search_history, sep='\n')
        return False
    elif target_url == URL_goal:
        print("\n\nGoal page found.")
        return False
    elif target_url == None:
        print("\n\nNo link found on: " + target_url)
    else:
        return True

#Crawls
while continue_crawl(article_chain, target_url):
    article_chain.append(target_url)

    response = requests.get(target_url).text
    soup = BeautifulSoup(response, 'html.parser')

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    target_url = None
    #loops through each element in a pages content until a link is found
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            target_url = "https://en.wikipedia.org" + element.find("a", recursive=False).get('href')
            break
    print(target_url)
