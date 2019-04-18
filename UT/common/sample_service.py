#!/usr/env/python
import sys
sys.path.insert(0,"..\\..\\src\\common")
from base_service import BaseService

class SampleService(BaseService):
	
	def __init__(self):
		print("Hello world!")
		super().__init__()


a = SampleService()
