from webrequests import make_request
from bs4 import BeautifulSoup

class Article:
  def __init__(self, title, url, parser) -> None:
    self.title = title
    self.url = url
    self.parser = parser
    self.response = None
    self.content = None
    self.soup = None

  def get_content(self):
    if self.response is None:
      resp = make_request(self.url)
      self.response = resp
    return self.response

  def get_soup(self):
    if self.soup is None:
      soup = BeautifulSoup(self.get_content())
      self.soup = soup
    return self.soup

  def parse_soup(self):
    if self.content is None:
      self.content = eval(self.parser)(self.get_soup())
    return self.content