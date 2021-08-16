from Core import Core
from Stmt import Stmt

"""
Class of the grammer <stmt-seq> ::= <stmt> | <stmt><stmt-seq>
"""
class StmtSeq:
    scanner = None
    stmt = None
    stmtseq = None

    # Parse-Tree processing by recursive descend
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
        # Check <Stmt-Seq>
        if(self.scanner.currentToken() != Core.END):
            self.stmtseq = StmtSeq()
            self.stmtseq.scanner = self.scanner
            self.stmtseq.parse()

    # printing two sub-trees: <stmt>, <stmt-seq>
    # @tab is the scale of indentation
    def print(self,tab):
        if (self.stmt != None):
            self.stmt.print(tab)

        if (self.stmtseq != None):
            self.stmtseq.print(tab)

    # executing two sub-trees: <stmt>, <stmt-seq>
    def execute(self):
        if (self.stmt != None):
            self.stmt.execute()
        if (self.stmtseq != None):
            self.stmtseq.execute()