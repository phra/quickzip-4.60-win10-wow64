#!/usr/bin/env python

import sys

def pattern_create(_type,_length):
  _type = _type.split(" ")
  if _type[0] == "trash":
    return _type[1] * _length
  elif _type[0] == "random":
    return ''.join(random.choice(string.lowercase) for i in range(_length))
  elif _type[0] == "pattern":
    _pattern = ''
    _parts = ['A', 'a', '0']
    while len(_pattern) != _length:
      _pattern += _parts[len(_pattern) % 3]
      if len(_pattern) % 3 == 0:
        _parts[2] = chr(ord(_parts[2]) + 1)
        if _parts[2] > '9':
          _parts[2] = '0'
          _parts[1] = chr(ord(_parts[1]) + 1)
          if _parts[1] > 'z':
            _parts[1] = 'a'
            _parts[0] = chr(ord(_parts[0]) + 1)
            if _parts[0] > 'Z':
              _parts[0] = 'A'
    return _pattern
  else:
    return "Not Found"

def main():
    if len(sys.argv) == 3:
        print pattern_create(sys.argv[1], int(sys.argv[2]))
    else:
        print "usage: python pattern.py <pattern|random|trash> <length>"

if __name__== "__main__":
    main()
