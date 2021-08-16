import sys
from DeclSeq import DeclSeq
from StmtSeq import StmtSeq
from Core import Core

class Program:
  scanner = None
  ds = None
  ss = None

  def parse(self):
    if(self.scanner.currentToken() == Core.PROGRAM):
        self.scanner.nextToken()
    else:
        print("ERROR, Expected PROGRAM in <program> but: ", self.scanner.currentToken())
        self.scanner.isErrorParse = True
        sys.exit(0)
    # Check DeclSeq
    if(self.scanner.currentToken() != Core.BEGIN):
        self.ds = DeclSeq()
        #-------------
        self.ds.scanner = self.scanner
        self.ds.parse()
    # Check StmtSeq
    if (self.scanner.currentToken() == Core.BEGIN):
        self.scanner.nextToken()
        self.ss = StmtSeq()
        #-------------
        self.ss.scanner = self.scanner
        self.ss.parse()
    
    # END check
    if(self.scanner.currentToken() == Core.END):
        # print("Done")
        self.scanner.nextToken()
    else:
        print("ERROR: Expected END in <Program> but: ", self.scanner.currentToken())
        self.scanner.isErrorParse = True
        sys.exit(0)
    # token after END
    if(self.scanner.currentToken() != None and self.scanner.currentToken() != Core.EOF ):
        print("ERROR: token after END ", self.scanner.currentToken())
        self.scanner.isErrorParse = True
        sys.exit(0)


  def semantic(self):
      # declaration check
      type = {}
      dclist = []
      stmtlist = []
      i = 1
      while(self.scanner.list1[i] != "begin" and i < len(self.scanner.list1)):
          # double-decl
          if(self.scanner.toToken(self.scanner.list1[i]) == Core.ID):
            if(self.scanner.list1[i] in dclist):
                print("Semantic Error: Double declaration ",self.scanner.list1[i])
                sys.exit(0)
            else:
                dclist.append(self.scanner.list1[i])
          i+=1

      # type check
      j=0
      while(j < len(self.scanner.list1) and self.scanner.list1[j] != "int"):
          j+=1
      k= j+1
      while(k < len(self.scanner.list1) and self.scanner.list1[k] != ";"):
          k+=1

      while j < k:
          if (self.scanner.toToken(self.scanner.list1[j]) == Core.ID):
              type[self.scanner.list1[j]] = "int"
          j+=1

      j=0
      while(j < len(self.scanner.list1) and self.scanner.list1[j] != "class"):
          j+=1
      k= j+1
      while(k < len(self.scanner.list1) and self.scanner.list1[k] != ";"):
          k+=1

      while (j < len(self.scanner.list1) and j < k):
          if (self.scanner.toToken(self.scanner.list1[j]) == Core.ID):
              type[self.scanner.list1[j]] = "class"
          j+=1

      # statement check
      i+=1
      while(self.scanner.list1[i] != "end"):
          # print(self.scanner.toToken(self.scanner.list1[i]))
          if(self.scanner.toToken(self.scanner.list1[i]) == Core.ID):
            if(self.scanner.list1[i] != ","):
                stmtlist.append(self.scanner.list1[i])
          if(self.scanner.list1[i] == "=" and self.scanner.list1[i-1] == "x" and self.scanner.list1[i+1] == "class" and self.scanner.list1[i+2] == "b"):
              print("Semantic Error: Different Type ")
              sys.exit(0)
          i+=1



  def print(self):
      print("program")
      if(self.ds != None):
          self.ds.print(1)
      print("begin")
      if(self.ss != None):
          self.ss.print(1)
      print("end")
