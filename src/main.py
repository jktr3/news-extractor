from network.network import Network
from network.article import Article
from utils import read_yml

cfg = read_yml('config.yml')

networks = {
  n: Network(
    sitemap_url = o['sitemap_url'],
    name = n,
    xml_parser = o['xml_parser'],
    article_parser=o['article_parser']) for n, o in cfg.items()
  }

print(networks)