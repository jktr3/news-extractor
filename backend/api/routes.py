from flask import Blueprint, abort, jsonify
from jinja2 import TemplateNotFound
from objects.network import Network
from utils import read_yml, timeit
from typing import Dict
import cachetools.func



cfg = read_yml('config.yml')
headlines = Blueprint('headlines', __name__)

@timeit
@cachetools.func.ttl_cache(maxsize=128, ttl=5 * 60)
def retrieve_and_shape_article_keywords() -> Dict[str, str]:
  networks = {
    n: Network(
      sitemap_url = o['sitemap_url'],
      name = n,
      xml_parser = o['xml_parser'],
      ) for n, o in cfg.items()
    }
  return {name: network.get_all_processed_articles() for name, network in networks.items()}

@headlines.route('/')
def show():
  try:
    article_headlines = retrieve_and_shape_article_keywords()
    return jsonify(article_headlines)
  except TemplateNotFound:
    abort(404)