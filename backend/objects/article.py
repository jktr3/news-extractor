from cleaner import clean_text_body


class Article:
  def __init__(self, title, url, publication_date, section) -> None:
    self.title = title
    self.url = url
    self.section = section
    self.publication_date = publication_date


  def get_article_keywords(self):
    return clean_text_body(self.title)