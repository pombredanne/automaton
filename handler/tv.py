# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort, Response, request, url_for, make_response, jsonify
from functools import update_wrapper
import json, sys
from pprint import pprint

import xbmcjsonlib, jsonrpclib

tv = Blueprint('tv', __name__)
xbmc = xbmcjsonlib.Server("http://jetway.pv.pingzero.net:8090/jsonrpc")
myth = jsonrpclib.Server("http://craft.pv.pingzero.net:8765")

@tv.route('/')
def index():
	return render_template('tv.html', page_title = "Television")


@tv.route('/Key', methods = ['GET', 'POST'])
def key():
	if request.method == 'POST':
		key = request.form['key']
		if   key=='info':		xbmc.Input.Info()
		elif key=='info':		xbmc.Input.ShowOSD()
		elif key=='back': 	xbmc.Input.Back()
		elif key=='up': 		xbmc.Input.Up()
		elif key=='home': 	xbmc.Input.Home()
		elif key=='left': 	xbmc.Input.Left()
		elif key=='select': 	xbmc.Input.Select()
		elif key=='right': 	xbmc.Input.Right()
		elif key=='pause': 	xbmc.Input.Left() # need to fix
		elif key=='down': 	xbmc.Input.Down()
		elif key=='context': xbmc.Input.ContextMenu()
		else: print "unknown key %s" % (key)
		return key
	else:
		return '', 500
		
@tv.route('/Remote')
def remote():
	return render_template("tv-remote.html", page_title = "Remote Control", scale='0.7')

@tv.route('/Recordings')
def recordings():
	items = myth.recordings()
	if len(items)==0:
		return render_template('tv-recordings.html', empty=True, page_title = 'Programmed TV Recordings', scale='0.7')
	return render_template('tv-recordings.html', items = items, page_title = 'Programmed TV Recordings', scale='0.7')

@tv.route('/LiveTV')
def livetv():
	items = myth.livetv()
	if len(items)==0:
		return render_template('tv-recordings.html', empty=True, page_title = 'Live TV Recordings', scale='0.7')
	return render_template('tv-recordings.html', items = items, page_title = 'Live TV Recordings', scale='0.7')
