from Core import Core
from Expr import Expr
import sys
from ID import Id

class Assign:
    scanner = None
    expr = None
    #-----------
    id = None
    id1 =None
    token = None

    def parse(self):
        if(self.scanner.currentToken() == Core.ID):
            # -----------
            self.id = self.scanner.getID()
            self.scanner.nextToken()
            if (self.scanner.currentToken() == Core.ASSIGN):
                self.scanner.nextToken()
                if (self.scanner.currentToken() == Core.NEW):
                    # -----------
                    self.token = "new"
                    self.scanner.nextToken()
                    if (self.scanner.currentToken() != Core.SEMICOLON):
                        print("Expect ';' in <Assign>, but ", self.scanner.currentToken())
                        self.scanner.isErrorParse = True
                        sys.exit(0)
                    else:
                        self.scanner.nextToken()
                elif(self.scanner.currentToken() == Core.CLASS):
                    # -----------
                    self.token = "class"
                    self.scanner.nextToken()
                    if (self.scanner.currentToken() == Core.ID):
                        # -----------
                        self.id1 = self.scanner.getID()
                        self.scanner.nextToken()
                        if (self.scanner.currentToken() != Core.SEMICOLON):
                            print("Expect ';' in <Assign>, but ", self.scanner.currentToken())
                            self.scanner.isErrorParse = True
                            sys.exit(0)
                        else:
                            self.scanner.nextToken()
                else:
                    self.expr = Expr()
                    self.expr.scanner = self.scanner
                    self.expr.parse()
                    if (self.scanner.currentToken() != Core.SEMICOLON):
                        print("Expect ';' in <Assign>, but ", self.scanner.currentToken())
                        self.scanner.isErrorParse = True
                        sys.exit(0)
                    else:
                        self.scanner.nextToken()
            else:
                print("Expect '=' in <Assign>, but ", self.scanner.currentToken())
                self.scanner.isErrorParse = True
                sys.exit(0)

    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"

        if(self.token != None):
            if(self.id1 != None):
                print(f"{inde}{self.id}={self.token} {self.id1};")
            else:
                print(f"{inde}{self.id}={self.token};")
        else:
            print(f"{inde}{self.id}={self.expr.print()};")
