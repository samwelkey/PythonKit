#!/usr/bin/env python
# encoding: utf-8

'''

@author: welkeyever

@file: WalkThroughADir.py

@time: 2018/5/14 下午10:22

@desc: 遍历一个路径，并打印出所有文件

'''

import os
import sys

if len(sys.argv) != 2:
    print('Only accept one PATH at a time.')
    sys.exit(0)
for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        print(os.path.join(root, name))

