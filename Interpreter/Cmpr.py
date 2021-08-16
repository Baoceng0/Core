from Core import Core
from Expr import Expr
import sys
"""
Class of the grammer <cond>::= <cmpr> | ! ( <cond> )
| <cmpr> or <cond>
"""
class Cmpr:
    scanner = None
    token = None
    expr = None
    expr1 =None

    # Parse-Tree processing by recursive descend
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
        else:
            print("Expect '=' in <cmpr>, but ", self.scanner.currentToken())

    # printing <expr> == <expr> | <expr> < <expr>
    # | <expr> <= <expr>
    def print(self):
        s = self.expr.print()
        s+= self.token
        s+= self.expr1.print()
        return s

    # executing <expr> == <expr> | <expr> < <expr>
    # | <expr> <= <expr>
    def execute(self):
        val = self.expr.execute()
        val1 = self.expr1.execute()
        if(self.token == "=="):
            return val1 == val
        elif(self.token == "<="):
            return val <= val1
        elif(self.token == "<"):
            return val < val1