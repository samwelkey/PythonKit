#!/bin/env python
# encoding: utf-8

'''

@author: welkeyever

@file: count_of_words.py

@time: 2018/6/8 下午15:47

@desc:统计文件中出现频率最高的前几个单词./

'''

import sys
from collections import Counter

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print('Usage: ./count_of_words.py somefile.txt 3, to print the most 3 frequent words in the file')
    sys.exit(0)

if len(sys.argv) == 3:
    tops = int(sys.argv[2])
else:
    tops = 3

filename = sys.argv[1]
with open(filename) as f:
    wordslist = f.read().split()
    word_counts = Counter(wordslist)
    topwords = word_counts.most_common(tops)
print(topwords)
