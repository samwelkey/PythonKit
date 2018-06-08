#!/usr/bin/env python
# encoding: utf-8

'''

@author: welkeyever

@file: pysearch.py

@time: 2018/6/8 下午8:11

@desc:

'''

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            print('###start pline: ')
            for pline in prevlines:
                print('$')
                print(pline, end='')
            print('###start line')
            print(line,end='')
            print('-'*20)

