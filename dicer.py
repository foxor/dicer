#!/usr/bin/env python

import random

def parse(string):
  num, size = [int(x) for x in string.split('d')]
  total = 0
  for _ in xrange(num):
    total += random.randint(1, size)
  return total

if __name__ == '__main__':
  import sys
  print parse(sys.argv[1])
