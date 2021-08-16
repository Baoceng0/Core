from Core import Core
from Expr import Expr
import sys

class Cmpr:
    scanner = None
    #-----------
    token = None
    expr = None
    expr1 =None

    def parse(self):
        if (self.scanner.currentToken() != Core.EOF):
            self.expr = Expr()
            self.expr.scanner = self.scanner
            self.expr.parse()
            if (self.scanner.currentToken() == Core.EQUAL or self.scanner.currentToken() == Core.LESS or self.scanner.currentToken() == Core.LESSEQUAL):
                if(self.scanner.currentToken() == Core.EQUAL):
                    self.token = "=="
                elif(self.scanner.currentToken() == Core.LESS):
                    self.token = "<"
                else:
                    self.token = "<="
                self.scanner.nextToken()

                if(self.scanner.currentToken() == Core.ID or self.scanner.currentToken() == Core.LPAREN or self.scanner.currentToken() == Core.CONST):
                    self.expr1 = Expr()
                    self.expr1.scanner = self.scanner
                    self.expr1.parse()
                else:
                    print("Error: Expect tokens of <Expr>, but ", self.scanner.currentToken())
                    self.scanner.isErrorParse = True
                    sys.exit(0)
		

                # if (self.scanner.currentToken() == Core.EQUAL):
                #     self.scanner.nextToken()
                # else:
                #     print("Expect '==' in <Cmpr>, but ", self.scanner.currentToken())
            # elif (self.scanner.currentToken() == Core.LESS):
            #         self.scanner.nextToken()
            #         if (self.scanner.currentToken() == Core.EQUAL):
            #             self.scanner.nextToken()
            #             expr1 = Expr()
            #             expr1.scanner = self.scanner
            #             expr1.parse()
            #         elif (self.scanner.currentToken() != Core.EOF):
            #             expr1 = Expr()
            #             expr1.scanner = self.scanner
            #             expr1.parse()
            #         else:
            #             print("Expect '<' in <Cmpr>, but ", self.scanner.currentToken())


        else:
            print("Expect '=' in <cmpr>, but ", self.scanner.currentToken())

    def print(self):
        s = self.expr.print()
        s+= self.token
        s+= self.expr1.print()
        return s
