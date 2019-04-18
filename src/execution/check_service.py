#!/usr/env/python
import sys
sys.path.insert(0,"..\\common")
from base_service import BaseService

class CheckService(BaseService):
	
	def __init__(self):
		print("Base Check Service")
		super().__init__()

