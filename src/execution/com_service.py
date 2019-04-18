#!/usr/env/python
import sys
sys.path.insert(0,"..\\common")
from base_service import BaseService

class ComService(BaseService):
	
	def __init__(self):
		print("Base Communication Service")
		super().__init__()

