1. Name: Cenglin Bao
#############################################################
2. Assign.py ----- file includes Assign class for <assign>
   Cmpr.py ----- file includes Cmpr class for <cmpr>
   Cond.py ----- file includes Cond class for <cond>
   Decl.py ----- file includes Decl class for <decl>
   DeclC.py ----- file includes DeclC class for <decl-class>
   DeclI.py ----- file includes DeclI class for <decl-int>
   DeclSeq.py ----- file includes DeclSeq class for <decl-seq>
   Expr.py ----- file includes Expr class for <expr>
   Factor.py ----- file includes Factor class for <factor>
   ID.py ----- file includes Id class for <id>
   Idlist.py ----- file includes Idlist class for <idlist>
   If.py ----- file includes If class for <if>
   In.py ----- file includes In class for <in>
   Loop.py ----- file includes Loop class for <loop>
   Main.py ----- file include Main class for running
   Out.py ----- file includes Out class for <out>
   Program.py ----- file includes Program class for <program>
   Scanner.py ----- file includes Scanner class for tokenizing
   Stmt.py ----- file includes Stmt class for <stmt>
   StmtSeq.py ----- file includes StmtSeq class for <stmt-seq>
   Term.py ----- file includes Term class for <term>
##################################################################
3. Wrote by Python

4. I spent most of time in the parse(), which needs to be familiar with Core grammer and the idea of recrusive descend. 
Also, the detailed design for parse error checking is critical to verify. Then I chose to implement the print(). If you can 
see the same content as the input file, it means that the parse tree works well. But indentation is a trouble after that. I
solved it by adding a '\t' everytime it get token "IF, ELSE, WHILE". For semantic checking, I had learned a lot for the lecture:
using data structures like Dictionary.

5. I firstly tested my program in Pycharm, by adding several print functions in the files. Then I tried to use tester.sh 
to check the output profession requires. 
 
   
