from Core import Core
from Cond import Cond
import StmtSeq
import sys

"""
Class of the grammer <loop> ::= while <cond> begin <stmt-seq> endwhile
"""
class Loop:
    scanner = None
    cond = None
    stmts = None

    # Parse-Tree processing by recursive descend
    def parse(self):
        # Check WHILE
        if (self.scanner.currentToken() == Core.WHILE):
            self.scanner.nextToken()
            if (self.scanner.currentToken() != Core.EOF and self.scanner.currentToken() != Core.BEGIN):
                self.cond = Cond()
                self.cond.scanner = self.scanner
                self.cond.parse()
                # Check BEGIN
                if (self.scanner.currentToken() == Core.BEGIN):
                    self.scanner.nextToken()
                    self.stmts = StmtSeq.StmtSeq()
                    self.stmts.scanner = self.scanner
                    self.stmts.parse()
                    # Check ENDWHILE
                    if (self.scanner.currentToken() == Core.ENDWHILE):
                        self.scanner.nextToken()
                    else:
                        print("ERROR: Expect 'endwhile' in <loop>, but ", self.scanner.currentToken())
                        self.scanner.isErrorParse = True
                        sys.exit(0)
                else:
                    print("ERROR:Expect ';' in <loop>, but ", self.scanner.currentToken())
                    self.scanner.isErrorParse = True
                    sys.exit(0)
            else:
                print("ERROR:Expect 'cond' in <loop>, but ", self.scanner.currentToken())
                self.scanner.isErrorParse = True
                sys.exit(0)
        else:
            print("ERROR:Expect 'WHILE' in <loop>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True
            sys.exit(0)

    # @tab is the scale of indentation
    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}while {self.cond.print()} begin")
        self.stmts.print(tab + 1)
        print(f"{inde}endwhile")

    # executing while <cond> begin <stmt-seq> endwhile
    def execute(self):
        if(self.cond != None):
            val = self.cond.execute()
            while(val == True):
                self.stmts.execute()
                val = self.cond.execute()

        else:
            print("Error: can't match in <loop>")
        if(len(self.scanner.map)!=0):
            upperScope = self.scanner.stack.pop()
            list = self.scanner.map.keys()
            for k in list:
                upperScope[k] = self.scanner.map.get(k)

            self.scanner.stack.append(upperScope)

        self.scanner.map = {}
