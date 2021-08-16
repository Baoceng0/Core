from Core import Core
from Factor import Factor


class Term:
    scanner = None
    #--------------
    fac = None
    term = None
    token = None

    def parse(self):
        if (self.scanner.currentToken() != Core.EOF):
            self.fac = Factor()
            self.fac.scanner = self.scanner
            self.fac.parse()
            if (self.scanner.currentToken() == Core.MULT):
                self.token = "*"
                self.scanner.nextToken()
                self.term = Term()
                self.term.scanner = self.scanner
                self.term.parse()

        else:
            print("Error: Expect !EOF in <Term>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True

    def print(self):
        #---------------
        s = ""
        if(self.fac != None):
            s += self.fac.print()
        else:
            return s

        if (self.token != None):
            s += self.token
            s += self.term.print()
        return s