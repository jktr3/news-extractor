from webrequests import make_request, parse_xml
from typing import List, Dict
from article import Article
from collections import Counter

class Network:
  def __init__(self, sitemap_url, name, xml_parser) -> None:
    self.sitemap_url = sitemap_url
    self.name = name
    self.xml_parser = xml_parser
    self.xml = self.get_remote_xml_sitemap()
    self.articles = self.set_articles()


  def __str__(self) -> str:
    return self.name


  def get_sitemap_articles(self) -> List[Dict[str, str]]:
    return eval(self.xml_parser)(self.xml)


  def set_articles(self):
    return [Article(
      title=a['title'],
      url=a['url']
      ) for a in self.get_sitemap_articles()]


  def get_remote_xml_sitemap(self):
    req_txt = make_request(self.sitemap_url)
    xml = parse_xml(req_txt)
    return xml


  def get_all_article_title_keywords(self) -> str:
    if self.articles:
      most_common_terms = set([i[0] for i in Counter([word for sublist in [a.get_clean_title() for a in self.articles] for word in sublist]).most_common(30)])
      return ", ".join([word for sublist in [a.get_clean_title() for a in self.articles] for word in sublist if word in most_common_terms])
    return ""