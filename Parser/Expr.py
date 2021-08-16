from Core import Core
from Term import Term


class Expr:
    scanner = None
    term = None
    #------------------
    expr = None
    token =None

    def parse(self):
        if (self.scanner.currentToken() != Core.EOF):
            self.term = Term()
            self.term.scanner = self.scanner
            self.term.parse()
            if (self.scanner.currentToken() == Core.ADD or self.scanner.currentToken() == Core.SUB):
                if (self.scanner.currentToken() == Core.ADD):
                    self.token = "+"
                else:
                    self.token = "-"
                self.scanner.nextToken()
                self.expr = Expr()
                self.expr.scanner = self.scanner
                self.expr.parse()

        else:
            print("Expect !EOF in <Expr>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True

    def print(self):
        #--------
        s = ""
        if(self.term != None):
            s += self.term.print()
        else:
            return s

        if (self.token != None):
            s+= self.token
            s += self.expr.print()

        return s