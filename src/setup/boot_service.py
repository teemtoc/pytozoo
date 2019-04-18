#!/usr/env/python
import sys
sys.path.insert(0,"..\\common")
from base_service import BaseService

class BootService(BaseService):
	
	def __init__(self):
		print("Base Boot Service")
		super().__init__()

