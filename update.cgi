#!/usr/bin/env python2.6
#  vim: ts=3 sw=3 ai
#
#  CGI for the sign

import bottle
from bottle import route, view, error, request


@route('/')
def index():
	stats = request.GET.get('q', '')
	fp = open('/dev/shm/sign1-stats', 'w')
	fp.write(stats)
	fp.close()
	return 'ok'


#####################################
bottle.run(server = bottle.CGIServer)
