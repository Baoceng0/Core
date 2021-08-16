from Core import Core
from Decl import Decl


"""
Class of the grammer <decl-seq> ::= <decl> | <decl><decl-seq>
"""
class DeclSeq:
    scanner = None
    dl = None
    ds = None

    # Parse-Tree processing by recrusive descend
    def parse(self):
        # Check Decl
        if (self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.CLASS ):
            # self.scanner.nextToken()
            self.dl = Decl()
            self.dl.scanner = self.scanner
            self.dl.parse()

        # Check DeclSeq
        if (self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.CLASS ):
            # self.scanner.nextToken()
            self.ds = DeclSeq()
            self.ds.scanner = self.scanner
            self.ds.parse()

    # executing <decl>,<decl-seq>
    def execute(self):
        if (self.dl != None):
            self.dl.execute()
        if (self.ds != None):
            self.ds.execute()

    # Semantic Check
    def semantic(self):
        if(self.dl != None):
           self.dl.semantic()

    # printing two sub-trees: <decl>,<decl-seq>
    def print(self,tab):
        if (self.dl != None):
            self.dl.print(tab)
        if (self.ds != None):
            self.ds.print(tab)