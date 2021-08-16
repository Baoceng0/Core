from Scanner import Scanner
from Scanner import Scanner1
import sys
from Program import Program

"""
main() will initialize the scanner with input files
argv1 - the text file
argv2 - the data file
"""
def main():

  S = Scanner(sys.argv[1])
  S1 = Scanner1(sys.argv[2])
  # store data into a list
  S.data = S1.list1

  # Start the process
  prog = Program()
  prog.scanner = S

  prog.parse()

  prog.execute()


if __name__ == "__main__":
    main()