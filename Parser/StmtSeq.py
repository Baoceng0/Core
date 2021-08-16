from Core import Core
from Stmt import Stmt

class StmtSeq:
    scanner = None
    stmt = None
    stmtseq = None


    def parse(self):


        # Check <Stmt>
        if(self.scanner.currentToken() != Core.EOF or self.scanner.currentToken() != Core.END):
            self.stmt = Stmt()
            self.stmt.scanner = self.scanner
            self.stmt.parse()

        if(self.scanner.currentToken() == Core.ENDWHILE or self.scanner.currentToken() == Core.ENDIF or self.scanner.currentToken() == Core.ELSE):
            return
        # Skip 'endIf' 'endwhile' 'else'
        if(self.scanner.currentToken() == Core.ENDIF or self.scanner.currentToken() == Core.ENDWHILE or
                self.scanner.currentToken() == Core.ELSE):
            self.scanner.nextToken()
            # return
        # Check <Stmt-Seq>
        if(self.scanner.currentToken() != Core.END):
            self.stmtseq = StmtSeq()
            self.stmtseq.scanner = self.scanner
            self.stmtseq.parse()

        # # Check END
        # if(self.scanner.currentToken() != Core.END):
        #     print("ERROR: Expected 'END' after StmtSeq, But: ",self.scanner.currentToken())
    def print(self,tab):
        if (self.stmt != None):
            self.stmt.print(tab)

        if (self.stmtseq != None):
            self.stmtseq.print(tab)