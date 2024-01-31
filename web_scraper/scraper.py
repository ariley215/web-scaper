import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Diego_Garcia"

response = requests.get(url)

wiki_soup = BeautifulSoup(response.text, "html.parser")

content_div = wiki_soup.find_all("div", {"class": "mw-content-ltr mw-parser-output"})

paragraph_with_sup = content_div.find_all('p', {'class': 'noprint Inline-Template Template-Fact'})

for paragraph in paragraph_with_sup:
  print(paragraph.text.strip())
 







# def get_citations_needed_count(url):


# def get_citations_needed_report(url):
