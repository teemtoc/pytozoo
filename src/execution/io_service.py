#!/usr/env/python
import sys
sys.path.insert(0,"..\\common")
from base_service import BaseService

class IOService(BaseService):
	
	def __init__(self):
		print("Base IO Service")
		super().__init__()

