#!/usr/bin/env python
# encoding: utf-8

'''

@author: welkeyever

@file: pyls.py

@time: 2018/5/24 下午9:58

@desc: Linux 'ls' tool in python

'''

import sys, os, time


def list_file(s):
    if os.path.isdir(s):
        file_type = 'Dir'
    else:
        file_type = "File"
    size = os.path.getsize(s)
    creation_seconds = os.path.getctime(s)
    create_row_time = time.localtime(creation_seconds)
    creation_time = time.strftime("%b %d %Y %H:%M:%S", create_row_time)
    total_length_of_a_col1 = 50
    total_length_of_a_col2 = 10
    total_length_of_a_col3 = 10
    space1 = total_length_of_a_col1 - len(s)
    space2 = total_length_of_a_col2 - len(file_type)
    space3 = total_length_of_a_col3 - len(str(size)+'B')
    print(s + ' ' * space1 + "\t" + file_type + ' ' * space2 + "\t" + str(size)+'B' + ' ' * space3 + "\t" + str(creation_time))


if len(sys.argv) == 1:
    path = str(os.getcwd())
else:
    path = sys.argv[1]
    if not os.path.isdir(path):
        list_file(path)
        sys.exit(0)


print('Location: ' + path)

listOfDir = os.listdir(path)

for s in listOfDir:
    list_file(path + '/' + s)
