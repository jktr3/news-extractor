from nltk.corpus import stopwords
import re
from typing import List


STOP_WORDS = set(stopwords.words('english'))

def clean_text_body(text: str) -> List[str]:
  word_list = apply_text_regex_rules(text.strip()).split(" ")
  return [apply_word_regex_rules(w) for w in word_list if (is_stop_word(apply_word_regex_rules(w).lower()) == False)]


def apply_text_regex_rules(text: str) -> str:
  return re.sub(r'^[a-zA-Z0-9_]+$', '', text)


def apply_word_regex_rules(text: str) -> str:
  text = text.replace("&apos;s","")
  return re.sub(r'[\W_]+', '', text)


def is_stop_word(text: str) -> bool:
  # nltk generic stopwords
  if text in STOP_WORDS:
    return True
  # stopwords in context of news headlines
  if text in ['opinion','says','know','amid','new']:
    return True

  return False