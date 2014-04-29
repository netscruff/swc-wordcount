#!/usr/bin/env python
from string import punctuation
from operator import itemgetter
import argparse

parser = argparse.ArgumentParser(description='Count word frequencies')
parser.add_argument('filename', action="store")
parser.add_argument('-n', action="store", type=int)
results = parser.parse_args()

N = results.n 
words = {}

words_gen = (word.strip(punctuation).lower() for line in open(results.filename) 
                                             for word in line.split())
                                          
for word in words_gen:
    words[word] = words.get(word, 0) + 1

top_words = sorted(words.iteritems(), key=itemgetter(1), reverse=True)[:N]

for word, frequency in top_words:
    print "%s: %d" % (word, frequency)
