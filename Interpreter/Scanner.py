from Core import Core
import re

class Scanner:
  # Constructor should open the file and find the first token
  index = 0
  SKIP = 0
  list1 = []
  isErrorParse = False

  # 3
  # map for local val
  # stack for global val
  # heap for reference
  map = {}
  stack =[]
  heap = []

  #3
  data = []
  indexD = 0


  def __init__(self, filename):

    with open(filename,'r') as f:
      myline = f.readline().strip(' ')
      while myline:
        # print("1 {myline}")
        # print(myline)
        if(myline != '\n'):
          # list.append(myline.split(' '))
          # print(myline)
        # print("2 {myline}")
          for s in myline.split(' '):
            # left strip
            s = s.lstrip('\n\t')
            # right strip
            s = s.rstrip('\n\t')
            if(s != ''):
              pre = 0
              Flag = True
              for i in range(len(s)):
                if (re.match(r'[A-Za-z0-9_]', s[i]) == None):
                  # Handle “<=” / ">=" / "=="
                  if (self.SKIP == 1):
                    self.SKIP = 0
                    continue
                  if ((i + 1) < len(s) and (s[i] == '<' or s[i] == '>') and s[i + 1] == '='):
                    if (s[pre:i] != '' and s[pre:i] != '\t'):
                      self.list1.append(s[pre:i])
                    if (s[i:i+2] != '' and s[i:i+2] != '\t'):
                      self.list1.append(s[i:i + 2])
                    pre = i + 2
                    self.SKIP = 1
                  elif ((i + 1) < len(s) and s[i] == '=' and s[i + 1] == '='):
                    if (s[pre:i] and s[pre:i] != '\t'):
                      self.list1.append(s[pre:i])
                    if (s[i:i + 2] != '' and s[i:i+2] != '\t'):
                      self.list1.append(s[i:i + 2])
                    pre = i + 2
                    self.SKIP = 1
                  else:
                    if(s[pre:i] != '' and s[pre:i] != '\t'):
                      self.list1.append(s[pre:i])
                    if (s[i] != '' and s[i] != '\t'):
                      self.list1.append(s[i])
                    pre = i + 1
                  Flag = False
              if (re.match(r'[A-Za-z0-9_]', s[-1]) != None and not Flag):
                self.list1.append(s[pre:])
              if(Flag):
                self.list1.append(s)
            # print(s)
        myline = f.readline().strip(' ')
      # myline = f.readlines()
      # for str in myline:
      #   list.append(str)
    # print(self.list1)
    # print(len(self.list1))
    # with open('15.code','w') as f:
    #   for str in self.list1:
    #     f.write(str+'\n')




  # nextToken should advance the scanner to the next token
  def nextToken(self):
    # print("list:",  self.list1)

    self.index += 1

  # currentToken should return the current token
  def currentToken(self):
    if(self.index == len(self.list1)):
      return Core.EOF

    # Keywords
    if (self.list1[self.index] == 'program'):
      return Core.PROGRAM
    if (self.list1[self.index] == 'begin'):
      return Core.BEGIN
    if (self.list1[self.index] == 'end'):
      return Core.END
    if (self.list1[self.index] == 'new'):
      return Core.NEW
    if (self.list1[self.index] == 'int'):
      return Core.INT
    if (self.list1[self.index] == 'define'):
      return Core.DEFINE
    if (self.list1[self.index] == 'endfunc'):
      return Core.ENDFUNC
    if (self.list1[self.index] == 'class'):
      return Core.CLASS
    if (self.list1[self.index] == 'extends'):
      return Core.EXTENDS
    if (self.list1[self.index] == 'endclass'):
      return Core.ENDCLASS
    if (self.list1[self.index] == 'if'):
      return Core.IF
    if (self.list1[self.index] == 'then'):
      return Core.THEN
    if (self.list1[self.index] == 'else'):
      return Core.ELSE
    if (self.list1[self.index] == 'while'):
      return Core.WHILE
    if (self.list1[self.index] == 'endwhile'):
      return Core.ENDWHILE
    if (self.list1[self.index] == 'endif'):
      return Core.ENDIF
    if (self.list1[self.index] == 'or'):
      return Core.OR
    if (self.list1[self.index] == 'input'):
      return Core.INPUT
    if (self.list1[self.index] == 'output'):
      return Core.OUTPUT

    # Identifier
    match = re.match(r'[A-Za-z]', self.list1[self.index])
    if (match != None):
      return Core.ID

    # Specials
    if (self.list1[self.index] == ','):
      return Core.COMMA
    elif (self.list1[self.index] == ';'):
      return Core.SEMICOLON
    elif (self.list1[self.index] == '('):
      return Core.LPAREN
    elif (self.list1[self.index] == ')'):
      return Core.RPAREN
    elif (self.list1[self.index] == '='):
      return Core.ASSIGN
    elif (self.list1[self.index] == '!'):
      return Core.NEGATION
    elif (self.list1[self.index] == '=='):
      return Core.EQUAL
    elif (self.list1[self.index] == '<'):
      return Core.LESS
    elif (self.list1[self.index] == '<='):
      return Core.LESSEQUAL
    elif (self.list1[self.index] == '+'):
      return Core.ADD
    elif (self.list1[self.index] == '-'):
      return Core.SUB
    elif (self.list1[self.index] == '*'):
      return Core.MULT

    # Constants
    try:
      if (int(self.list1[self.index]) <= 1023 and int(self.list1[self.index]) >= 0):
        return Core.CONST
      elif(int(self.list1[self.index]) > 1023 or int(self.list1[self.index]) < 0):
        print("ERROR: Const out of the boundary 0-1023: ", self.list1[self.index])
        return Core.ERROR
      else:
        return Core.ERROR
    except:
      print("ERROR: Invalid input: ", self.list1[self.index])
      return Core.ERROR

  # If the current token is ID, return the string value of the identifier
	# Otherwise, return value does not matter
  def getID(self):
    return self.list1[self.index]

  # If the current token is CONST, return the numerical value of the constant
	# Otherwise, return value does not matter
  def getCONST(self):
    return self.list1[self.index]

  #
  def toToken(self, word):
    # Keywords
    if (word == 'program'):
      return Core.PROGRAM
    if (word == 'begin'):
      return Core.BEGIN
    if (word == 'end'):
      return Core.END
    if (word == 'new'):
      return Core.NEW
    if (word == 'int'):
      return Core.INT
    if (word == 'define'):
      return Core.DEFINE
    if (word == 'endfunc'):
      return Core.ENDFUNC
    if (word == 'class'):
      return Core.CLASS
    if (word == 'extends'):
      return Core.EXTENDS
    if (word == 'endclass'):
      return Core.ENDCLASS
    if (word == 'if'):
      return Core.IF
    if (word == 'then'):
      return Core.THEN
    if (word == 'else'):
      return Core.ELSE
    if (word == 'while'):
      return Core.WHILE
    if (word == 'endwhile'):
      return Core.ENDWHILE
    if (word == 'endif'):
      return Core.ENDIF
    if (word == 'or'):
      return Core.OR
    if (word== 'input'):
      return Core.INPUT
    if (word == 'output'):
      return Core.OUTPUT

    # Identifier
    match = re.match(r'[A-Za-z]', word)
    if (match != None):
      return Core.ID

    # Specials
    if (word == ','):
      return Core.COMMA
    elif (word == ';'):
      return Core.SEMICOLON
    elif (word == '('):
      return Core.LPAREN
    elif (word == ')'):
      return Core.RPAREN
    elif (word == '='):
      return Core.ASSIGN
    elif (word == '!'):
      return Core.NEGATION
    elif (word == '=='):
      return Core.EQUAL
    elif (word == '<'):
      return Core.LESS
    elif (word == '<='):
      return Core.LESSEQUAL
    elif (word == '+'):
      return Core.ADD
    elif (word == '-'):
      return Core.SUB
    elif (word == '*'):
      return Core.MULT

    # Constants
    try:
      if (int(word) <= 1023 and int(word) >= 0):
        return Core.CONST
      elif (int(word) > 1023 or int(word) < 0):
        print("ERROR: Const out of the boundary 0-1023: ", word)
        return Core.ERROR
      else:
        return Core.ERROR
    except:
      print("ERROR: Invalid input: ", word)
      return Core.ERROR

class Scanner1:
  # Constructor should open the file and find the first token
  index = 0
  SKIP = 0
  list1 = []
  isErrorParse = False

  def __init__(self, filename):

    with open(filename,'r') as f:
      myline = f.readline().strip(' ')
      while myline:
        # print("1 {myline}")
        # print(myline)
        if(myline != '\n'):
          # list.append(myline.split(' '))
          # print(myline)
        # print("2 {myline}")
          for s in myline.split(' '):
            # left strip
            s = s.lstrip('\n\t')
            # right strip
            s = s.rstrip('\n\t')
            if(s != ''):
              pre = 0
              Flag = True
              for i in range(len(s)):
                if (re.match(r'[A-Za-z0-9_]', s[i]) == None):
                  # Handle “<=” / ">=" / "=="
                  if (self.SKIP == 1):
                    self.SKIP = 0
                    continue
                  if ((i + 1) < len(s) and (s[i] == '<' or s[i] == '>') and s[i + 1] == '='):
                    if (s[pre:i] != '' and s[pre:i] != '\t'):
                      self.list1.append(s[pre:i])
                    if (s[i:i+2] != '' and s[i:i+2] != '\t'):
                      self.list1.append(s[i:i + 2])
                    pre = i + 2
                    self.SKIP = 1
                  elif ((i + 1) < len(s) and s[i] == '=' and s[i + 1] == '='):
                    if (s[pre:i] and s[pre:i] != '\t'):
                      self.list1.append(s[pre:i])
                    if (s[i:i + 2] != '' and s[i:i+2] != '\t'):
                      self.list1.append(s[i:i + 2])
                    pre = i + 2
                    self.SKIP = 1
                  else:
                    if(s[pre:i] != '' and s[pre:i] != '\t'):
                      self.list1.append(s[pre:i])
                    if (s[i] != '' and s[i] != '\t'):
                      self.list1.append(s[i])
                    pre = i + 1
                  Flag = False
              if (re.match(r'[A-Za-z0-9_]', s[-1]) != None and not Flag):
                self.list1.append(s[pre:])
              if(Flag):
                self.list1.append(s)
            # print(s)
        myline = f.readline().strip(' ')