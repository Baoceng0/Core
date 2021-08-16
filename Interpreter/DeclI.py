from Core import Core
from Idlist import Idlist
import sys
"""
Class of the grammer <decl-int> ::= int <id-list> ;
"""
class DeclI:
    scanner = None
    idlist = None

    # Parse-Tree processing by recrusive descend
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

    # Semantic Check
    def semantic(self):
        if(self.idlist != None):
            self.idlist.semantic()

    # printing <ld-list>
    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}int {self.idlist.print()};")
        # if (self.idlist != None):
        #     self.idlist.print()

    def execute(self):
        s = ""
        if (self.idlist != None):
            s =self.idlist.execute()
        if(s != ""):
            vals = s.split(',')
            # print("declint",vals)
            for val in vals:
                # print("declint1", val)
                # print("declintmap", self.scanner.map)
                self.scanner.map[val] = "0"
        # print(self.scanner.map)
