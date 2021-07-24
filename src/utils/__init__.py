import yaml
import functools
from typing import Any


@functools.lru_cache(maxsize=1)
def read_yml(filepath) -> Any:
  with open(filepath, 'r') as stream:
    try:
      return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      return exc