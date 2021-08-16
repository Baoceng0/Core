from Core import Core
from Term import Term

"""
Class of the grammer <expr>::=<term> | <term> + <expr> | <term> – <expr>
"""
class Expr:
    scanner = None
    term = None
    expr = None
    token =None

    # Parse-Tree processing by recursive descend
    def parse(self):
        if (self.scanner.currentToken() != Core.EOF):
            self.term = Term()
            self.term.scanner = self.scanner
            self.term.parse()
            if (self.scanner.currentToken() == Core.ADD or self.scanner.currentToken() == Core.SUB):
                if (self.scanner.currentToken() == Core.ADD):
                    self.token = "+"
                else:
                    self.token = "-"
                self.scanner.nextToken()
                self.expr = Expr()
                self.expr.scanner = self.scanner
                self.expr.parse()
        else:
            print("Expect !EOF in <Expr>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True

    #printing <term> | <term> + <expr> | <term> – <expr>
    def print(self):
        s = ""
        if(self.term != None):
            s += self.term.print()
        else:
            return s

        if (self.token != None):
            s+= self.token
            s += self.expr.print()
        return s

    #executing <term> | <term> + <expr> | <term> – <expr>
    def execute(self):
        val = self.term.execute()
        if (type(val) != type(1) and self.scanner.toToken(val) == Core.ID):
            # print("need?")
            if (val in self.scanner.map):
                val = int(self.scanner.map[val])
            else:
                map = self.scanner.stack.pop()
                val = int(map[val])
                self.scanner.stack.append(map)
        else:
            val = int(val)
        # token = +, so calculate <term> + <expr>
        if(self.token == "+"):
            add = self.expr.execute()
            # if add is ID, find its value in map
            if (type(val) != type(1) and self.scanner.toToken(add) == Core.ID):
                # print("need?")
                if (add in self.scanner.map):
                    add = int(self.scanner.map[val])
                else:
                    map = self.scanner.stack.pop()
                    add = int(map[add])
                    self.scanner.stack.append(map)
            else:
                add = int(add)
            val += add
        elif(self.token == "-"):
            minus = int(self.expr.execute())
            if (type(val) != type(1) and self.scanner.toToken(minus) == Core.ID):
                if (minus in self.scanner.map):
                    minus = int(self.scanner.map[minus])
                else:
                    map = self.scanner.stack.pop()
                    minus = int(map[minus])
                    self.scanner.stack.append(map)
            else:
                minus = int(minus)
            val -= minus

        return val