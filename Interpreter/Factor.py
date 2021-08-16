from Core import Core
import Expr
import sys
"""
Class of the grammer id | const | ( <expr> )
"""
class Factor:
    scanner = None
    id = None
    expr = None
    option = 0

    def parse(self):
        if (self.scanner.currentToken() == Core.ID):
            self.id = self.scanner.getID()
            self.scanner.nextToken()
        elif (self.scanner.currentToken() == Core.CONST):
            self.option = 1
            self.id =self.scanner.getCONST()
            self.scanner.nextToken()
        elif(self.scanner.currentToken() == Core.LPAREN):
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

    # printing id | const | ( <expr> )
    def print(self):
        s = self.id
        if(self.id == "("):
            s += self.expr.print()
            s += ")"
        return s

    # executing id | const | ( <expr> )
    def execute(self):
        if self.option == 1:
            return int(self.id)
        if(self.id != "("):
            if(self.id in self.scanner.map):
                return self.scanner.map[self.id]
            else:
                if(len(self.scanner.stack) !=0):
                    return self.id
        else:
            self.id = self.expr.execute()
            return self.id
