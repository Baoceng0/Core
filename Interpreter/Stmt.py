from Core import Core
from Assign import Assign
from If import If
from Loop import Loop
from In import In
from Out import Out
from Decl import Decl

"""
Class of the grammer <stmt> ::= <assign> | <if> | <loop> | <in> | <out> | <decl>
"""
class Stmt:
    scanner = None
    help = None
    level = 0

    def __init__(self):
        None

    # Parse-Tree processing by recursive descend
    def parse(self):
        # Go to <Assign>
        if (self.scanner.currentToken() == Core.ID):
            assign = Assign()
            assign.scanner = self.scanner
            assign.parse()
            self.help = assign

        # Go to <if>
        elif (self.scanner.currentToken() == Core.IF):
            if1 = If()
            if1.scanner = self.scanner
            if1.parse()
            self.help = if1

        # Go to <loop>
        elif (self.scanner.currentToken() == Core.WHILE):
            loop = Loop()
            loop.scanner = self.scanner
            loop.parse()
            self.help = loop

        # Go to <in>
        elif (self.scanner.currentToken() == Core.INPUT):
            input = In()
            input.scanner = self.scanner
            input.parse()
            self.help = input

        # Go to <output>
        elif (self.scanner.currentToken() == Core.OUTPUT):
            output = Out()
            output.scanner = self.scanner
            output.parse()
            self.help = output

        # Go to <decl>
        else:
            decl = Decl()
            decl.scanner = self.scanner
            decl.parse()
            self.help = decl

    # printing <assign> | <if> | <loop> | <in> | <out> | <decl>
    # @tab is the scale of indentation
    def print(self,tab):
        self.help.print(tab + self.level)

    # executing the help object
    def execute(self):
        if(self.help != None):
            self.help.execute()
        else:
            print("Error: can't match in <Stmt>")
