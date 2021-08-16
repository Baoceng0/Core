from Core import Core
from DeclI import DeclI
from DeclC import DeclC
import sys
"""
Class of the grammer <decl> ::= <decl-int> | <decl-class>
"""
class Decl:
    scanner = None
    declI = None
    declC = None

    # Parse-Tree processing by recrusive descend
    def parse(self):
        # Check Decl
        if (self.scanner.currentToken() == Core.INT):
            self.scanner.nextToken()
            self.declI = DeclI()
            self.declI.scanner = self.scanner
            self.declI.parse()

        # Check DeclSeq
        elif (self.scanner.currentToken() == Core.CLASS):
            self.scanner.nextToken()
            self.declC = DeclC()
            self.declC.scanner = self.scanner
            self.declC.parse()
        else:
            print("ERROR: Expect 'Class'/'Int' in <Decl> but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True
            sys.exit(0)

    # Semantic Check
    def semantic(self):
        if(self.declI != None):
            self.declI.semantic()
        # if (self.declC != None):
        #     self.declC.semantic()

    # printing <decl-int>, <decl-class>
    def print(self,tab):
        if (self.declI != None):
            self.declI.print(tab)
        if (self.declC != None):
            self.declC.print(tab)

    # executing <decl-int>, <decl-class>
    def execute(self):
        if (self.declI != None):
            self.declI.execute()
        if (self.declC != None):
            self.declC.execute()