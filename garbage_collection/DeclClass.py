from IdList import IdList
from Core import Core

class DeclClass:
	
	def parse(self, parser):
		parser.expectedToken(Core.CLASS)
		parser.scanner.nextToken()
		self.list = IdList()
		self.list.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("class ", end='')
		self.list.print()
		print(";\n", end='')

	def execute(self, executor):
		self.list.executeClassIdList(executor)