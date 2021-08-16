from Core import Core

from Cmpr import Cmpr
"""
Class of the grammer <cond>::= <cmpr> | ! ( <cond> )
| <cmpr> or <cond>
"""
class Cond:
    scanner = None
    cond = None
    cond1 = None
    token = None
    cmpr = None

    # Parse-Tree processing by recursive descend
    def parse(self):
        if (self.scanner.currentToken() == Core.NEGATION):
            self.token = "!"
            self.scanner.nextToken()
            if (self.scanner.currentToken() == Core.LPAREN):
                self.scanner.nextToken()
                self.cond = Cond()
                self.cond.scanner = self.scanner
                self.cond.parse()

                if (self.scanner.currentToken() == Core.RPAREN):
                    self.scanner.nextToken()
                else:
                    print("Expect ')' in <cond>, but ", self.scanner.currentToken())

            else:
                print("Expect '(' in <cond>, but ", self.scanner.currentToken())
        elif(self.scanner.currentToken() != Core.EOF):
            self.cmpr = Cmpr()
            self.cmpr.scanner = self.scanner
            self.cmpr.parse()
            if(self.scanner.currentToken() == Core.OR):
                self.token = "or"
                self.scanner.nextToken()
                self.cond1 = Cond()
                self.cond1.scanner = self.scanner
                self.cond1.parse()
            
        else:
            print("Expect !EOF in <if>, but ", self.scanner.currentToken())

    # printing <cmpr> | ! ( <cond> )
    # | <cmpr> or <cond>
    def print(self):
        s=""
        if(self.token == "!"):
            s+="!("
            s+=self.cond.print()
            s+=")"
        elif(self.token == "or"):
            s+=self.cmpr.print()
            s+= " or "
            s+=self.cond1.print()
        else:
            s+=self.cmpr.print()
        return s

    # executing cmpr
    def execute(self):
        if(self.token == None):
            val = self.cmpr.execute()
            return val
        elif(self.token == "or"):
            val = self.cmpr.execute()
            val1 = self.cond1.execute()
            return val or val1
        elif(self.token == "!"):
            val = self.cond.execute()
            return not val
