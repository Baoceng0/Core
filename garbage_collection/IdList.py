from Id import Id
from Core import Core

class IdList:
	
	def parse(self, parser):
		self.id = Id()
		self.id.parse(parser)
		if parser.scanner.currentToken() == Core.COMMA:
			parser.scanner.nextToken()
			self.list = IdList()
			self.list.parse(parser)
	
	def print(self):
		self.id.print()
		if hasattr(self, 'list'):
			print(",", end='')
			self.list.print()

	def executeIntIdList(self, executor):
		self.id.executeIntAllocate(executor)
		if hasattr(self, 'list'):
			self.list.executeIntIdList(executor)

	def executeClassIdList(self, executor):
		self.id.executeClassAllocate(executor)
		if hasattr(self, 'list'):
			self.list.executeClassIdList(executor)