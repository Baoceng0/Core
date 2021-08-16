from Core import Core
from DeclI import DeclI
from DeclC import DeclC
import sys

class Decl:
    scanner = None
    declI = None
    declC = None

    def parse(self):
        # Check Decl
        if (self.scanner.currentToken() == Core.INT):
            self.scanner.nextToken()
            self.declI = DeclI()
            self.declI.scanner = self.scanner
            self.declI.parse()

        # if (self.scanner.currentToken() == Core.SEMICOLON):
        #     self.scanner.nextToken()
        # else:
        #     print("In Decl")
        # Check DeclSeq
        elif (self.scanner.currentToken() == Core.CLASS):
            self.scanner.nextToken()
            self.declC = DeclC()
            self.declC.scanner = self.scanner
            self.declC.parse()
        else:
            # print("last one", self.scanner.list1[:self.scanner.index-1])

            print("ERROR: Expect 'Class'/'Int' in <Decl> but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True
            sys.exit(0)

    def semantic(self):
        if(self.declI != None):
            self.declI.semantic()
        # if (self.declC != None):
        #     self.declC.semantic()

    def print(self,tab):
        if (self.declI != None):
            self.declI.print(tab)
        if (self.declC != None):
            self.declC.print(tab)
