from Core import Core
from Cond import Cond
import StmtSeq
import sys

class Loop:
    scanner = None
    cond = None
    stmts = None

    def parse(self):
        if (self.scanner.currentToken() == Core.WHILE):
            self.scanner.nextToken()
            # This used to be or 5/29
            if (self.scanner.currentToken() != Core.EOF and self.scanner.currentToken() != Core.BEGIN):
                self.cond = Cond()
                self.cond.scanner = self.scanner
                self.cond.parse()
                if (self.scanner.currentToken() == Core.BEGIN):
                    self.scanner.nextToken()
                    self.stmts = StmtSeq.StmtSeq()
                    self.stmts.scanner = self.scanner
                    self.stmts.parse()
                    if (self.scanner.currentToken() == Core.ENDWHILE):
                        self.scanner.nextToken()
                    else:
                        print("ERROR: Expect 'endwhile' in <loop>, but ", self.scanner.currentToken())
                        self.scanner.isErrorParse = True
                        sys.exit(0)
                        # print("this one ", self.scanner.list1[self.scanner.index])
                        # print("last one ", self.scanner.list1[self.scanner.index-1])
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

    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}while {self.cond.print()} begin")
        self.stmts.print(tab + 1)
        print(f"{inde}endwhile")
