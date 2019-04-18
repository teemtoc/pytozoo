#!/usr/env/python

class BaseService():
	thread_list = {}
	running = False
	socket_list = []
	signal_socket = None
	
	def __init__(self):
		self.running = True
		self.thread_list = {}
		self.initialize_socket()
		self.initialize_main_loop()
	
	def __del__(self):
		self.running = False
		for thread in self.thread_list.keys():
			self.thread_list[thread].stop()

	def set_socket_list(self,socket_list):
		self.socket_list = socket_list
		
	def initialize_main_loop(self):
		raise NotImplementedError

	def initialize_socket(self):
		raise NotImplementedError

	def get_signal_socket(self):
		return signal_socket

	def register_thread(self, thread_id, params):
		raise NotImplementedError()

	def remove_thread(self, thread_id):
		self.thread_list[thread].stop()
		del(self.thread_list[thread])

	def get_module_status(self):
		return running

	def receive_signals(self):
		raise NotImplementedError

	def send_signals(self, signal):
		raise NotImplementedError

	def set_thread_variable(self, thread_id, key, value):
		raise NotImplementedError

	def get_thread_variable(self, thread_id, key):
		raise NotImplementedError	

