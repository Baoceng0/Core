from Core import Core
from Cond import Cond
import StmtSeq

class If:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.cond = Cond()
		self.cond.parse(parser)
		parser.expectedToken(Core.THEN)
		parser.scanner.nextToken()
		self.ss1 = StmtSeq.StmtSeq()
		self.ss1.parse(parser)
		if parser.scanner.currentToken() == Core.ELSE:
			parser.scanner.nextToken()
			self.ss2 = StmtSeq.StmtSeq()
			self.ss2.parse(parser)
		parser.expectedToken(Core.ENDIF)
		parser.scanner.nextToken()
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("if ", end='')
		self.cond.print()
		print(" then\n", end='')
		self.ss1.print(indent+1)
		if hasattr(self, 'ss2'):
			for x in range(indent):
				print("  ", end='')
			print("else\n", end='')
			self.ss2.print(indent+1)
		for x in range(indent):
			print("  ", end='')
		print("endif\n", end='')

	def execute(self, executor):
		condition = self.cond.execute(executor)
		executor.pushLocalScope()
		if condition:
			self.before = len(executor.heapSpace)
			self.ss1.execute(executor)
		elif hasattr(self, 'ss2'):
			self.ss2.execute(executor)
		# print("h",executor.heapSpace)
		# print("s",executor.stackSpace)
		# print('s',len(executor.stackSpace))
		if executor.gc != 0 and len(executor.heapSpace) != self.before:
			executor.gc -= 1
			print("gc:", executor.gc)
		executor.popLocalScope()
