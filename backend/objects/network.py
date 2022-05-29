from typing import List, Dict
from collections import Counter
from utils.webrequests import make_request, parse_xml
from objects.article import Article


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
    if self.name == "WSJ":
      import pdb; pdb.set_trace()
    return eval(self.xml_parser)(self.xml)


  def set_articles(self):
    a = [Article(
      title=a['title'],
      section=a['section'],
      url=a['url'],
      publication_date=a['publication_date'],
      ) for a in self.get_sitemap_articles()]
    return sorted(a, key=lambda x: x.publication_date, reverse=True)


  def get_remote_xml_sitemap(self):
    req_txt = make_request(self.sitemap_url)
    xml = parse_xml(req_txt)
    return xml


  def get_all_processed_articles(self) -> str:
    if self.articles:
      # Build a map of all top terms mentioned
      most_common_terms = set([i[0] for i in Counter([word for sublist in [a.get_article_keywords() for a in self.articles] for word in sublist]).most_common(5)])
      most_common_map = {}
      for a in self.articles:
        keywords = a.get_article_keywords()
        for kw in keywords:
          if kw in most_common_terms:
            if kw not in most_common_map:
              most_common_map[kw] = {"count": 0, "frequency": 0.0}
              most_common_map[kw]["count"] = 0
            else:
              most_common_map[kw]["count"] += 1

            most_common_map[kw]["frequency"] = most_common_map[kw]['count'] / len(self.articles)

      return {
        'most_common_keywords': most_common_map,
        'articles': [
          {
            'title': a.title,
            'section': a.section,
            'date': a.publication_date,
            'url': a.url,
            'keywords': a.get_article_keywords()
          } for a in self.articles
          ]
      }

    return ""