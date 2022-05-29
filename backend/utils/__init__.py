import yaml
import functools
from typing import Any
import time


@functools.lru_cache(maxsize=1)
def read_yml(filepath) -> Any:
  with open(filepath, 'r') as stream:
    try:
      return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      return exc


def timeit(method):
  def timed(*args, **kw):
    ts = time.time()
    result = method(*args, **kw)
    te = time.time()
    if 'log_time' in kw:
      name = kw.get('log_name', method.__name__.upper())
      kw['log_time'][name] = int((te - ts) * 1000)
    else:
      print(f'{method.__name__}  {(te - ts) * 1000} ms')
    return result
  return timed