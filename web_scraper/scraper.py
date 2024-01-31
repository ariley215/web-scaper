import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Diego_Garcia'

response = requests.get(url)

wiki_soup = BeautifulSoup(response.text, 'html.parser')


paragraphs = wiki_soup.p['class']
for paragraph in paragraphs:
  print(paragraph)
  
  
  # noprint Inline-Template Template-Fact
# def get_citations_needed_count(url):
  
  
# def get_citations_needed_report(url):