from Core import Core
import Idlist
import sys
"""
Class of the grammer <decl-class> ::= class <id-list> ;
"""
class DeclC:
    scanner = None
    idlist = None

    # Parse-Tree processing by recrusive descend
    def parse(self):
        # Check Decl-Class
        if (self.scanner.currentToken() == Core.ID):
            self.idlist = Idlist.Idlist()
            self.idlist.scanner = self.scanner
            self.idlist.parse()
        else:
            print("ERROR: Expect 'ID' in <Decl-Class>")
            self.scanner.isErrorParse = True
            sys.exit(0)

        # Check ';'
        if (self.scanner.currentToken() == Core.SEMICOLON):
            self.scanner.nextToken()
        else:
            print("Expect ';' in the end <Decl-Class>")
            self.scanner.isErrorParse = True
            sys.exit(0)

    # printing <ld-list>
    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}class {self.idlist.print()};")

    # executing <ld-list>
    def execute(self):
        s = ""
        if (self.idlist != None):
            s =self.idlist.execute()
        # s has several ids
        if(s != ""):
            vals = s.split(',')
            for val in vals:
                self.scanner.map[val] = "None"
                self.scanner.heap.append(val)

