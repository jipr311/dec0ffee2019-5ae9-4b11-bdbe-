#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#simple_websocket_server is 
#https://pypi.org/project/simple-websocket-server/
#pip install simple-websocket-server
from simple_websocket_server import WebSocketServer, WebSocket


class SimpleEcho(WebSocket):
	def handle(self):
		print("new msg: " + self.data)
		self.send_message("queloque!")

	def connected(self):
		print(self.address, 'connected')

	def handle_close(self):
		print(self.address, 'closed')


server = WebSocketServer('', 8765, SimpleEcho)
server.serve_forever()
