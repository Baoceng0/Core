from Formals import Formals
from Id import Id
from Core import Core

class FuncCall:
	
    def parse(self, parser):
        parser.scanner.nextToken()
        self.funcName = Id()
        self.funcName.parse(parser)
        parser.expectedToken(Core.LPAREN)
        parser.scanner.nextToken()
        self.actualParams = Formals()
        self.actualParams.parse(parser)
        parser.expectedToken(Core.RPAREN)
        parser.scanner.nextToken()
        parser.expectedToken(Core.SEMICOLON)
        parser.scanner.nextToken()
	
    def print(self, indent):
        for x in range(indent):
            print("  ", end='')
        self.name.print()
        print("(", end='')
        self.actualParams.print()
        print(");\n", end='')

    def execute(self, executor):
        # print("heap", executor.heapSpace)
        formalParams = executor.getFormalParams(self.funcName)
        body = executor.getBody(self.funcName)
        executor.pushFrame(formalParams, self.actualParams)
        before = len(executor.heapSpace)
        body.execute(executor)
        # print("heap", executor.heapSpace)
        # print("stack", executor.stackSpace)
        # print("global", executor.globalSpace)
        executor.popFrame()
        if executor.gc != 0 and len(executor.heapSpace) != before:
            executor.gc -= 1
            print("gc:", executor.gc)
