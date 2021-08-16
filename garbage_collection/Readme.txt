1. Name: Cenglin Bao
#############################################################
2. Assign.py ----- file includes Assign class for <assign>
   Cmpr.py ----- file includes Cmpr class for <cmpr>
   Cond.py ----- file includes Cond class for <cond>
   Decl.py ----- file includes Decl class for <decl>
   DeclClass.py ----- file includes DeclC class for <decl-class>
   DeclInt.py ----- file includes DeclI class for <decl-int>
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
   Executor.py ----- file includes Executor class for tokenizing
   Stmt.py ----- file includes Stmt class for <stmt>
   StmtSeq.py ----- file includes StmtSeq class for <stmt-seq>
   Term.py ----- file includes Term class for <term>
   FuncDecl.py ----- file includes Term class for <func-decl>
   Formals.py ----- file includes Term class for <formals>
   FuncCall.py ----- file includes Term class for <func-call>
##################################################################
3. Wrote by Python

4. As we don't really need to collect the memory pieces, I just used a variable "index" instead of a list
 in Executor.py to monitor the changes in the heap. In the <Assign>, if a variable is initialized (x= new y), the index would increment
The chanllenge is that, how should I handle the initialized vars in the local scope(if, while, func-call), which are deposed when the running over the scope.
I created a val to record the size of heap before it going to those local scope areas. And in the end of running, checking the current size of heap. If current size
bigger than the old size, the index decreases and prints the gc messages. 

5. For this lab, my coding is based on the project4, which highly consisted of the canonical of project3. So most of part would look same. 
I firstly tested my program in Pycharm, by adding several print functions in the files. Then I tried to use tester.sh 
to check the output profession requires. 
 
   
