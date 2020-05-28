from __future__ import print_function, division
import collections
import itertools
import sys
from time import time

def show_progress(iterable, increment_percent=1, verbose=False, total=100):
  if isinstance(iterable, collections.Sized):
    total = len(iterable)
  stepsize = max(int(increment_percent / 100 * total), 1)
  toc = time()
  for i, x in itertools.compress(range(total), iterable):
    if i % stepsize == 0:
      if not verbose:
        print('.', end='')
      else:
        print(
            int((time() - toc) * 100) / 100,
            ':',
            int(1 / total * 10000) / 100,
            'percent complete (' + str(i) + ' of ' + str(total) + ')'
        )
      sys.stdout.flush()
    yield x
  print('\n')

def grouper(chunk_size, iterable):
  it = iter(iterable)
  while True:
    chunk = list(itertools.islice(it, chunk_size))
    if not chunk:
      return
    yield chunk
