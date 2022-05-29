import requests
import xml.etree.ElementTree as ET


def make_request(url):
  req = requests.get(url)
  # import pdb; pdb.set_trace()
  if req.status_code != 200:
    print(req.status_code)
    raise ValueError
  return req.text


def parse_xml(resp_txt):
  return ET.fromstring(resp_txt)


def parse_xml_file(filepath):
  return ET.parse(filepath)