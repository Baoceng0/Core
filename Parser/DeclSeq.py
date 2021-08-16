from Core import Core
from Decl import Decl



class DeclSeq:
    scanner = None
    dl = None
    ds = None

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

    def semantic(self):
        if(self.dl != None):
           self.dl.semantic()

    def print(self,tab):
        if (self.dl != None):
            self.dl.print(tab)
        if (self.ds != None):
            self.ds.print(tab)