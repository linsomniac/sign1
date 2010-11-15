#!/usr/bin/env python2.6
#  vim: ts=3 sw=3 ai
#
#  CGI for the sign

from bottle import route, view

@route('/')
@view('index.html')
def hello():
	import time, sys, math, os

	reloadseconds = int(math.ceil(61 - (time.time()%60)))
	time_now = time.strftime('%l:%M')
	meridian = time.strftime('%P')
	date = time.strftime('%a %d')
	week_day = time.strftime('%a')
	month_day = time.strftime('%d').lstrip('0')
	month = time.strftime('%B')

	mdi = int(month_day)
	mdiDict = { 0 : 'th', 1 : 'st', 2 : 'nd', 3 : 'rd', 4 : 'th', 5 : 'th',
			6 : 'th', 7 : 'th', 8 : 'th', 9 : 'th' }
	if (mdi >= 10 and mdi <= 20) or mdi == 30:
		month_day_suffix = 'th'
	else:
		month_day_suffix = mdiDict.get(mdi % 10, '')

	temperature = ''
	if os.path.exists('/tmp/wunder.temp'):
		fp = open('/tmp/wunder.temp', 'r')
		temperature = fp.read().strip()
		fp.close()

	wind = ''
	if os.path.exists('/tmp/wunder.wind'):
		fp = open('/tmp/wunder.wind', 'r')
		wind = fp.read().strip()
		fp.close()

	forecast = ''
	if os.path.exists('/tmp/google.forecast'):
		fp = open('/tmp/google.forecast', 'r')
		forecast = fp.read().strip()
		fp.close()

	return(locals())

import bottle
bottle.debug(True)
bottle.run(server = bottle.CGIServer)
