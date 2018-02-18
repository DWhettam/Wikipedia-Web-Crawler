import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Special:Random')
html = response.text

article_chain = []

soup = BeautifulSoup(html, 'html.parser')
print("Starting Page: " + soup.title.string)
target_url = soup.find(id = 'mw-content-text').p.a.get('href')

#Checks if crawler is looping, if page has no links,  or Philosophy has been found
def continue_crawl(search_history, target_url):
    if target_url in search_history:
        print("\n\nCrawler is looping. \n" + target_url + " has previously been visited\n\n")
        print("Crawler history: ")
        print(*search_history, sep='\n')
        return False
    elif target_url == '/wiki/Philosophy':
        print("\n\nPhilosophy page found.")
        print("Chain of Links:")
        print(*search_history, sep='\n')
        return False
    elif target_url == None:
        print("\n\nNo link found on: " + target_url)
        print("Chain of Links:")
        print(*search_history, sep='\n')
    else:
        return True

#Crawls
while continue_crawl(article_chain, target_url):
    article_chain.append(target_url)

    full_url = "https://en.wikipedia.org" + target_url
    response = requests.get(full_url).text
    soup = BeautifulSoup(response, 'html.parser')

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    target_url = None
    #loops through each element in a pages content until a link is found
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            target_url = element.find("a", recursive=False).get('href')
            break
    print(target_url)
