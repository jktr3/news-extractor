from cleaner import clean_text_body


class Article:
  def __init__(self, title, url) -> None:
    self.title = title
    self.url = url


  def get_clean_title(self):
    return clean_text_body(self.title)