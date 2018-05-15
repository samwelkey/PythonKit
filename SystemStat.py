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
print("")
nowTime = time.localtime(time.time())
if nowTime.tm_hour < 12:
    greeting = 'Good morning!'
elif nowTime < 18:
    greeting = 'Good afternoon！'
else:
    greeting = 'Good evening！'
print('Now is: ' + time.strftime('%Y-%m-%d %H:%M:%S', nowTime) + ' ' + greeting)
print("")

print('System version: ' + sys.version)
print("")

cpuUsageCommand = "echo \"$(top -l 1 | awk '/CPU usage/';)\""
cpuString = os.popen(cpuUsageCommand)
cpuUsage = cpuString.readline()
print(cpuUsage)
memUsageCommand = "echo \"$(top -l 1 | awk '/PhysMem/';)\""
memString = os.popen(memUsageCommand)
memUsage = memString.readline();

print(memUsage)






