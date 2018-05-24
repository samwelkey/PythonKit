#!/usr/bin/env python
# encoding: utf-8

'''

@author: welkeyever

@file: pycurl.py

@time: 2018/5/18 上午12:23

@desc:无返回值的curl一个网址，第一个参数为网址，第二个参数为curl的次数，第三个参数为可选参数，设定每一个curl的间隔秒数,若只有地址则退化为普通curl。./

'''

import sys, urllib2, time
if len(sys.argv) == 1 or len(sys.argv) > 4:
    print('Usage: ./pycurl.py http://abc.com 10 1')
    sys.exit(0)
url = sys.argv[1]


if len(sys.argv) == 2:
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    text = res.read().decode("utf-8")
    print(text)
    sys.exit(0)

times = sys.argv[2]
count = 0

while True:
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    count += 1
    print('curled url: ' + url + ' ' +str(count) + ' times')
    if count == int(times):
        sys.exit(0)
    if len(sys.argv) == 4:
        time.sleep(int(sys.argv[3]))
    else:
        time.sleep(1)