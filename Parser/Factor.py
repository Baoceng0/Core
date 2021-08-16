from Core import Core
import Expr
import sys

class Factor:
    scanner = None
    #------------
    id = None
    expr = None

    def parse(self):
        if (self.scanner.currentToken() == Core.ID):
            # ------------
            self.id = self.scanner.getID()
            self.scanner.nextToken()
        elif (self.scanner.currentToken() == Core.CONST):
            # -------------
            self.id =self.scanner.getCONST()
            self.scanner.nextToken()
            # print("info1 ", self.scanner.currentToken())
        elif(self.scanner.currentToken() == Core.LPAREN):
            # *****
            self.id = "("
            self.scanner.nextToken()
            self.expr = Expr.Expr()
            self.expr.scanner = self.scanner
            self.expr.parse()
            if(self.scanner.currentToken() == Core.RPAREN):
                self.scanner.nextToken()
            else:
                print("Expect ')' in <factor>, but ", self.scanner.currentToken())
                self.scanner.isErrorParse = True
                sys.exit(0)
        else:
            print("ERROR: Expect !EOF in <factor>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True
            sys.exit(0)

    def print(self):
        s = self.id
        # print("hell! in factor")
        if(self.id == "("):
            # print("here! in factor")
            s += self.expr.print()
            s += ")"
        return s
