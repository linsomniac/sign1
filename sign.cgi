#!/usr/bin/env python
#  vim: ts=3 sw=3 ai
#
#  CGI for the sign

import time, sys, math, os

print 'Content-type: text/html'
print

fp = open('index.html', 'r')
data = fp.read()
fp.close()

template = {}
template['reloadseconds'] = int(math.ceil(61 - (time.time()%60)))
template['time'] = time.strftime('%l:%M')
template['meridian'] = time.strftime('%P')
template['date'] = time.strftime('%a %d')
template['week_day'] = time.strftime('%a')
template['month_day'] = time.strftime('%d').lstrip('0')
template['month'] = time.strftime('%B')

mdi = int(template['month_day'])
mdiDict = { 0 : 'th', 1 : 'st', 2 : 'nd', 3 : 'rd', 4 : 'th', 5 : 'th',
		6 : 'th', 7 : 'th', 8 : 'th', 9 : 'th' }
if (mdi >= 10 and mdi <= 20) or mdi == 30:
	template['month_day_suffix'] = 'th'
else:
	template['month_day_suffix'] = mdiDict.get(mdi % 10, '')

template['temperature'] = ''
if os.path.exists('/tmp/wunder.temp'):
	fp = open('/tmp/wunder.temp', 'r')
	template['temperature'] = fp.read().strip()
	fp.close()

template['wind'] = ''
if os.path.exists('/tmp/wunder.wind'):
	fp = open('/tmp/wunder.wind', 'r')
	template['wind'] = fp.read().strip()
	fp.close()

template['forecast'] = ''
if os.path.exists('/tmp/google.forecast'):
	fp = open('/tmp/google.forecast', 'r')
	template['forecast'] = fp.read().strip()
	fp.close()

sys.stdout.write(data % template)
