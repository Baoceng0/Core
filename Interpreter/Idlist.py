from Core import Core
import sys
from ID import Id

"""
Class of the grammer <id-list> ::= id | id , <id-list>
"""
class Idlist:
    scanner = None
    idlist = None
    id = None
    comma = False
    idname = None

    # 0 - single val
    # 1 - mult val
    option = 0

    # Parse-Tree processing by recrusive descend
    def parse(self):
        # Check Decl-int
        if (self.scanner.currentToken() == Core.ID):
            self.idname = self.scanner.getID()
            self.id = Id(self.idname,None,None,None)
            self.scanner.nextToken()
            if(self.scanner.currentToken() == Core.COMMA):
                self.option = 1
                self.comma = True
                self.scanner.nextToken()
                self.idlist = Idlist()
                self.idlist.scanner = self.scanner
                self.idlist.parse()
        else:
            print("ERROR: Expected 'ID' in <id-list>,but ",self.scanner.currentToken())
            self.scanner.isErrorParse = True
            sys.exit(0)

    # printing strings
    def print(self):
        s = self.idname
        if(self.comma == True):
            s += ","
            s += self.idlist.print()
        return s

    # return val names back
    def execute(self):
        s = self.idname
        if(self.comma == True):
            s += ","
            s += self.idlist.print()
        return s
