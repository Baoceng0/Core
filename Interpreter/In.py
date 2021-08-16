from Core import Core
import sys


"""
Class of the grammer <in> ::= input id ;
"""
class In:
    scanner = None
    token = None

    # Parse-Tree processing by recursive descend
    def parse(self):
        if (self.scanner.currentToken() == Core.INPUT):
            self.scanner.nextToken()
            if (self.scanner.currentToken() == Core.ID):
                self.token = self.scanner.getID()
                self.scanner.nextToken()
                if (self.scanner.currentToken() == Core.SEMICOLON):
                    self.scanner.nextToken()

                else:
                    print("Expect ';' in <IN>, but ", self.scanner.currentToken())
                    self.scanner.isErrorParse = True
            else:
                print("Expect 'ID' in <IN>, but ", self.scanner.currentToken())
                self.scanner.isErrorParse = True
        else:
            print("Expect 'INPUT' in <IN>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True

    # @tab is the scale of indentation
    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}input {self.token};")

    # executing  <in> ::= input id ;
    def execute(self):
        # get input value to local scope
        if(self.token in self.scanner.map):
            self.scanner.map[self.token] = self.scanner.data[self.scanner.indexD]
            self.scanner.indexD += 1
            # boundary check
            if(self.scanner.indexD == len(self.scanner.data)):
                print("Error: the input file doesn't have enough data!")
                sys.exit()
        # get input value to global scope
        else:
            map = self.scanner.stack.pop()
            map[self.token] = self.scanner.data[self.scanner.indexD]
            self.scanner.indexD += 1
            self.scanner.stack.append(map)
            # boundary check
            if(self.scanner.indexD == len(self.scanner.data)):
                print("Error: the input file doesn't have enough data!")
                sys.exit()