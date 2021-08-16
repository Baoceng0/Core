from Core import Core
import Idlist
import sys

class DeclC:
    scanner = None
    idlist = None


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

    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}class {self.idlist.print()};")
