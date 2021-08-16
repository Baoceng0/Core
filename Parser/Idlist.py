from Core import Core
import sys
from ID import Id


class Idlist:
    scanner = None
    idlist = None
    #------------
    id = None
    comma = False
    idname = None


    def parse(self):
        # Check Decl-int
        if (self.scanner.currentToken() == Core.ID):
            # ------------
            self.idname = self.scanner.getID()
            self.id = Id(self.idname,None,None,None)
            self.scanner.nextToken()
            if(self.scanner.currentToken() == Core.COMMA):
                #---------
                self.comma = True
                self.scanner.nextToken()
                self.idlist = Idlist()
                self.idlist.scanner = self.scanner
                self.idlist.parse()
            # else:
            #     print("ERROR: Expected ',' in <id-list>,but ", self.scanner.currentToken())
        else:
            print("ERROR: Expected 'ID' in <id-list>,but ",self.scanner.currentToken())
            self.scanner.isErrorParse = True
            sys.exit(0)

    def print(self):
        s = self.idname
        if(self.comma == True):
            s += ","
            s += self.idlist.print()
        return s
