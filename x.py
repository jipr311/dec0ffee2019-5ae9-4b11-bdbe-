#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import curdir, sep
import cgi
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import logging

#HOST_NAME = '0.0.0.0'
# !!!REMEMBER TO CHANGE THIS!!!
HOST_NAME = '127.0.0.1'
PORT_NUMBER = 8123 


class MyHandler(BaseHTTPRequestHandler):
	def do_DELETE(s):
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write(b'{\"hello\":\"do_DELETE!\"}')
		
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
	def do_XOCE(s):
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write(b'{\"xA\":3.1415927, \"y\":\"am gone!!\"}')
		
	def do_PATCH(s):
		s.send_response(410)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write(b'{\"hello\":\"do_PATCH!\", \"x\":\"am gone!!\"}')
				
	def do_PUT(s):
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()
		s.wfile.write(b'{\"hello\":\"PUT!\"}')
		
	def do_GET(s):
		"""Respond to a GET request."""
		if s.path=="/":
			s.path="/index.html"
		try:
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
				f = open(curdir + sep + s.path, 'rb') 
				s.send_response(200)
				s.send_header('Content-type',mimetype)
				s.end_headers()
				#print('f.reading4')
				#print(f.read())
				#print('f.reading/end4')
				s.wfile.write(f.read())
				f.close()
			return
		except IOError:
			s.send_response(404)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			# If someone went to "http://something.somewhere.net/foo/bar/",
			# then s.path equals "/foo/bar/".
			f = open(curdir + sep + '404.html', 'rb')
			#print('f.reading404')
			#print(f.read())
			#print('f.reading/end404') 
			s.wfile.write(f.read())
			f.close()
			#s.send_error(404,'File Not Found: %s' % s.path)
			
			
	def do_POST(self):
		#self.send_header("Content-type", "application/json")
		
		content_len = int(self.headers.get('content-length', 0))
		post_body = self.rfile.read(content_len)
		print(post_body)
		#print form.getvalue("x")
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		#print form.getvalue("bin")
		self.wfile.write(b'{\"hello\":\"mundo!\"}')

def run(server_class=HTTPServer, handler_class=MyHandler, port=PORT_NUMBER):
    logging.basicConfig(level=logging.INFO)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
    
if __name__ == '__main__':
	run()
