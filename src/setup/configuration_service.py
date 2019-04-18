#!/usr/env/python
import sys
sys.path.insert(0,"..\\common")
from base_service import BaseService

class ConfigurationService(BaseService):
	
	def __init__(self):
		print("Base Configuration Service")
		super().__init__()

