from Core import Core
from Factor import Factor

"""
Class of the grammer <term> ::= <factor> | <factor> * <term>
"""
class Term:
    scanner = None
    fac = None
    term = None
    token = None

    # Parse-Tree processing by recursive descend
    def parse(self):
        if (self.scanner.currentToken() != Core.EOF):
            self.fac = Factor()
            self.fac.scanner = self.scanner
            self.fac.parse()
            if (self.scanner.currentToken() == Core.MULT):
                self.token = "*"
                self.scanner.nextToken()
                self.term = Term()
                self.term.scanner = self.scanner
                self.term.parse()

        else:
            print("Error: Expect !EOF in <Term>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True

    #printing <factor> | <factor> * <term>
    def print(self):
        s = ""
        if(self.fac != None):
            s += self.fac.print()
        else:
            return s

        if (self.token != None):
            s += self.token
            s += self.term.print()
        return s

    # executing <factor> | <factor> * <term>
    def execute(self):
        val = self.fac.execute()
        if (type(val) != type(1) and self.scanner.toToken(val) == Core.ID):

            if (val in self.scanner.map):
                val = int(self.scanner.map[val])
            else:
                map = self.scanner.stack.pop()
                val = int(map[val])
                self.scanner.stack.append(map)
        if(self.token == "*"):
            val1 = self.term.execute()
            if(type(val1) != type(1) and self.scanner.toToken(val1) == Core.ID):
                if(val1 in self.scanner.map):
                    val1 = int(self.scanner.map[val1])
                else:
                    map = self.scanner.stack.pop()
                    val1 = int(map[val1])
                    self.scanner.stack.append(map)
            val1 = int(val1)
            val = int(val)
            val *= val1
        return val