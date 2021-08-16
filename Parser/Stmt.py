from Core import Core
from Assign import Assign
from If import If
from Loop import Loop
from In import In
from Out import Out
from Decl import Decl


class Stmt:
    scanner = None
    help = None
    level = 0

    def __init__(self):
        None

    def parse(self):
        # Go to <Assign>
        if (self.scanner.currentToken() == Core.ID):
            # print("info00 ", self.scanner.currentToken())
            assign = Assign()
            assign.scanner = self.scanner
            assign.parse()
            # ----------
            self.help = assign

        # Go to <if>
        elif (self.scanner.currentToken() == Core.IF):
            if1 = If()
            if1.scanner = self.scanner
            if1.parse()
            # ----------
            self.help = if1
            # self.level = 1


        # Go to <loop>
        elif (self.scanner.currentToken() == Core.WHILE):
            loop = Loop()
            loop.scanner = self.scanner
            loop.parse()
            # ----------
            self.help = loop
            # self.level = 1

        # Go to <in>
        elif (self.scanner.currentToken() == Core.INPUT):
            input = In()
            input.scanner = self.scanner
            input.parse()
            # ----------
            self.help = input

        # Go to <output>
        elif (self.scanner.currentToken() == Core.OUTPUT):
            output = Out()
            output.scanner = self.scanner
            output.parse()
            # ----------
            self.help = output

        # Go to <decl>
        else:
            # print("info01 ", self.scanner.currentToken())
            decl = Decl()
            decl.scanner = self.scanner
            decl.parse()
            # ----------
            self.help = decl

    def print(self,tab):

            self.help.print(tab + self.level)
