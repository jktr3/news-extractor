from network import Network
from utils import read_yml
import timeit

cfg = read_yml('config.yml')

networks = {
  n: Network(
    sitemap_url = o['sitemap_url'],
    name = n,
    xml_parser = o['xml_parser'],
    ) for n, o in cfg.items()
  }

# import pdb; pdb.set_trace()
# Write all keywords to txt files
for name, network in networks.items():
  all_words = network.get_all_article_title_keywords()
  with open(f'../{name}.txt', 'w') as f:
    f.write(all_words)
