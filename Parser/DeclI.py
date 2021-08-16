from Core import Core
from Idlist import Idlist
import sys

class DeclI:
    scanner = None
    idlist = None


    def parse(self):
        # Check Decl-int
        if (self.scanner.currentToken() == Core.ID):
            self.idlist = Idlist()
            self.idlist.scanner = self.scanner
            self.idlist.parse()
        else:
            print("Error: Expect 'ID' in <Decl-int>")
            self.scanner.isErrorParse = True
            sys.exit(0)

        # Check ';'
        if (self.scanner.currentToken() == Core.SEMICOLON):
            self.scanner.nextToken()
        else:
            print("Error: Expect ';' in the end <Decl-int>")
            self.scanner.isErrorParse = True
            sys.exit(0)

    def semantic(self):
        if(self.idlist != None):
            self.idlist.semantic()
        # if (self.declC != None):
        #     self.declC.semantic()

    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}int {self.idlist.print()};")
        # if (self.idlist != None):
        #     self.idlist.print()
