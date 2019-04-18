#!/usr/env/python
import sys
sys.path.insert(0,"..\\common")
from base_service import BaseService

class DiscoveryService(BaseService):
	
	def __init__(self):
		print("Base Discovery Service")
		super().__init__()

