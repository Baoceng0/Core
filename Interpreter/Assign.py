from Core import Core
from Expr import Expr
import sys
from ID import Id
"""
Class of the grammer <assign> ::= id = <expr> ; | id = new ; | id = class id ;
"""
class Assign:
    scanner = None
    expr = None
    id = None
    id1 =None
    token = None
    option = 0

    # Parse-Tree processing by recursive descend
    def parse(self):
        if(self.scanner.currentToken() == Core.ID):
            # -----------
            self.id = self.scanner.getID()
            self.scanner.nextToken()
            if (self.scanner.currentToken() == Core.ASSIGN):
                self.scanner.nextToken()
                if (self.scanner.currentToken() == Core.NEW):
                    self.option = 3
                    self.token = "new"
                    self.scanner.nextToken()
                    if (self.scanner.currentToken() != Core.SEMICOLON):
                        print("Expect ';' in <Assign>, but ", self.scanner.currentToken())
                        self.scanner.isErrorParse = True
                        sys.exit(0)
                    else:
                        self.scanner.nextToken()
                elif(self.scanner.currentToken() == Core.CLASS):
                    #3
                    self.option = 2
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
                    #3
                    self.option = 1
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

    # printing id = <expr> ; | id = new ; | id = class id ;
    # @tab is the scale of indentation
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

    # executing id = <expr> ; | id = new ; | id = class id ;
    def execute(self):
        if(self.option == 1):
            if(self.id in self.scanner.map):

                val = self.expr.execute()
                if(val not in self.scanner.heap and self.scanner.map[self.id] == "None"):
                    print("Illegal assign to class type!")
                    sys.exit(0)
                self.scanner.map[self.id] = val

            else:
                val = self.expr.execute()
                upperScope = self.scanner.stack.pop()
                # print("val ", val)
                if(val not in self.scanner.heap and upperScope[self.id]  == "None"):
                    print("Illegal assign to class type!")
                    sys.exit(0)
                upperScope[self.id] = val
                self.scanner.stack.append(upperScope)
        elif(self.option == 3):
                self.scanner.heap.append(0)
                if (self.id in self.scanner.map):
                    # self.scanner.map[self.id] = len(self.scanner.heap) -1
                    self.scanner.map[self.id] = 0
                else:
                    upperScope = self.scanner.stack.pop()
                    if (self.id not in self.scanner.heap and upperScope[self.id] == "None"):
                        print("Illegal assign to class type!")
                        sys.exit(0)
                    # upperScope[self.id] = len(self.scanner.heap) -1
                    self.scanner.map[self.id] = 0
                    self.scanner.stack.append(upperScope)
        elif(self.option == 2):
                if(self.id in self.scanner.map):
                    self.scanner.map[self.id] = self.id1
                else:
                    upperScope = self.scanner.stack.pop()
                    if (self.id not in self.scanner.heap and upperScope[self.id] == "None"):
                        print("Illegal assign to class type!")
                        sys.exit(0)
                    upperScope[self.id] = self.id1
                    self.scanner.stack.append(upperScope)




