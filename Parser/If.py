from Core import Core
from Cond import Cond
import StmtSeq
import sys

class If:
    scanner = None
    stmts = None
    stmts1 = None
    cond = None
    token = None

    def parse(self):
        if (self.scanner.currentToken() == Core.IF):
            self.scanner.nextToken()
            if (self.scanner.currentToken() != Core.THEN):
                # self.scanner.nextToken()
                self.cond = Cond()
                self.cond.scanner = self.scanner
                self.cond.parse()

                if (self.scanner.currentToken() == Core.THEN):
                    self.scanner.nextToken()
                    self.stmts = StmtSeq.StmtSeq()
                    self.stmts.scanner = self.scanner
                    self.stmts.parse()
                else:
                    print("Expect 'Then' in <If>, but ", self.scanner.currentToken())
                    self.scanner.isErrorParse = True
                    #sys.exit(0)

                # ELSE or ENDIF
                if (self.scanner.currentToken() == Core.ENDIF):
                    self.scanner.nextToken()
                elif(self.scanner.currentToken() == Core.ELSE):
                    self.token = "else"
                    self.scanner.nextToken()
                    self.stmts1 = StmtSeq.StmtSeq()
                    self.stmts1.scanner = self.scanner
                    self.stmts1.parse()
                    if (self.scanner.currentToken() == Core.ENDIF):
                        self.scanner.nextToken()
                    else:
                        print("Expect 'ENDIF' in <IF>, but ", self.scanner.currentToken())
                        self.scanner.isErrorParse = True
	                #sys.exit(0)
                else:
                    print("Expect 'ENDIF' in <IF>, but ", self.scanner.currentToken())
                    self.scanner.isErrorParse = True
	            #sys.exit(0)
            else:
                print("Expect 'Cond' in <IF>, but ", self.scanner.currentToken())
                self.scanner.isErrorParse = True
	        #sys.exit(0)
        else:
            print("Expect 'IF' in <if>, but ", self.scanner.currentToken())
            self.scanner.isErrorParse = True
	    #sys.exit(0)

    def print(self,tab):
        inde = ""
        for _ in range(tab):
            inde += "\t"
        print(f"{inde}if {self.cond.print()} then")
        self.stmts.print(tab+1)
        if(self.token != None):
            print(f"{inde}else")
            self.stmts1.print(tab+1)
        print(f"{inde}endif")
