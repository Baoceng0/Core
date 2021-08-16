from Scanner import Scanner
# from Core import Core
import sys
from Program import Program

def main():
  # Initialize the scanner with the input file
  S = Scanner(sys.argv[1])



  # print(S.list1)
  prog = Program()
  prog.scanner = S
  # prog.semantic()
  #
  prog.parse()
  if(S.isErrorParse != True):
    #
    prog.semantic()
    #
    prog.print()
  else:
    print("Error in Parser, stop!")

if __name__ == "__main__":
    main()