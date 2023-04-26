import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

site = "https://support.paysera.com/index.php?/payseraeng/Knowledgebase/List"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)

links_decs = {'link': [],
              "description": []}

for div in soup.findAll("div", {"class": "boxcontainer"}):
    for link in div.findAll('a', href=True):
        print(link.get('href'))
        print(link.contents[0])
        links_decs['link'].append(link.get('href'))
        links_decs['description'].append(link.contents[0])

pd.DataFrame.from_dict(links_decs).to_csv("data/pairs_link_desc.csv")
