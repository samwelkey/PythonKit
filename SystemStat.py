#!/usr/bin/env python
# encoding: utf-8

'''

@author: welkeyever

@file: SystemStat.py

@time: 2018/5/14 下午10:48

@desc:

'''

import sys, os, time

print('Welcome ' + os.getlogin() + '!')
nowTime = time.localtime(time.time())
if nowTime.tm_hour < 12:
    greeting = 'Good morning!'
elif nowTime < 18:
    greeting = 'Good afternoon！'
else:
    greeting = 'Good evening！'
print('Now is: ' + time.strftime('%Y-%m-%d %H:%M:%S', nowTime) + ' ' + greeting)

print('System version: ' + sys.version)

print('CPU status: ')

print('Memory Status: ')






