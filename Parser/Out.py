from Core import Core
from Expr import Expr

class Out:
    scanner = None
    #---------
    token = None
    expr = None

    def parse(self):
        # Check 'OUTPUT'
        if (self.scanner.currentToken() == Core.OUTPUT):
            self.scanner.nextToken()
            if (self.scanner.currentToken() != Core.EOF or self.scanner.currentToken() == Core.SEMICOLON):
                self.expr = Expr()
                self.expr.scanner = self.scanner
                self.expr.parse()
                # Check ';'
                if (self.scanner.currentToken() == Core.SEMICOLON):
                    self.scanner.nextToken()

                else:
                    print("Expect ';' in <out>, but ", self.scanner.currentToken())
                    self.scanner.isErrorParse = True
            else:
                print("Expect 'expr' in <out>, but ", self.scanner.currentToken())
                self.scanner.isErrorParse = True
        else:
            print("Expect 'Output' in <out>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True

    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}output {self.expr.print()};")