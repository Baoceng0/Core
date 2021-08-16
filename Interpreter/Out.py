from Core import Core
from Expr import Expr

"""
Class of the grammer output <expr> ;
"""
class Out:
    scanner = None
    token = None
    expr = None

    # Parse-Tree processing by recursive descend
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

    # printing output <expr> ;
    # @tab is the scale of indentation
    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}output {self.expr.print()};")

    # executing <expr> ;
    def execute(self):
        val = self.expr.execute()
        if(len(self.scanner.map)==0):
            map = self.scanner.stack.pop()
            self.scanner.stack.append(map)
            if(self.scanner.toToken(str(abs(val))) == Core.CONST):
                print(val)
            else:
                print(map[val])
        else:
            if(self.scanner.toToken(str(abs(val))) == Core.CONST):
                print(val)
            else:
                print(self.scanner.map[val])
