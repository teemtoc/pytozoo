#!/usr/env/python
import sys
sys.path.insert(0,"..\\common")
from base_service import BaseService

class ExecutionService(BaseService):
	
	def __init__(self):
		print("Base BoExecution Service")
		super().__init__()

