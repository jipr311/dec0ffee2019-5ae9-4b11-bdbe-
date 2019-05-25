#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import time
from os import curdir, sep
from sys import argv

class S(BaseHTTPRequestHandler):
	def do_DELETE(s):
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write("{\"hello\":\"do_DELETE!\"}")
		
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
	def do_XOCE(s):
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write("{\"xA\":3.1415927, \"y\":\"am gone!!\"}")
		
	def do_PATCH(s):
		s.send_response(410)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write("{\"hello\":\"do_PITCH!\", \"x\":\"am gone!!\"}")
				
	def do_PUT(s):
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write("{\"hello\":\"PUT!\"}")
		
	def do_GET(s):
		"""Respond to a GET request."""
		if s.path=="/":
			#s.path="/index_example2.html"
			s.path="/index.html"
		try:
			#Check the file extension required and
			#set the right mime type
			sendReply = False
			if s.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if s.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if s.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if s.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if s.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + s.path) 
				s.send_response(200)
				s.send_header('Content-type',mimetype)
				s.end_headers()
				s.wfile.write(f.read())
				f.close()
			return
		except IOError:
			s.send_response(404)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			# If someone went to "http://something.somewhere.net/foo/bar/",
			# then s.path equals "/foo/bar/".
			f = open(curdir + sep + '404.html') 
			s.wfile.write(f.read())
			f.close()
			#s.send_error(404,'File Not Found: %s' % s.path)
			
			
	def do_POST(self):
		#self.send_header("Content-type", "application/json")
		
		content_len = int(self.headers.getheader('content-length', 0))
		post_body = self.rfile.read(content_len)
		print(post_body)
		#print form.getvalue("x")
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		#print form.getvalue("bin")
		self.wfile.write("{\"hello\":\"mundo!\"}")

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':


    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
