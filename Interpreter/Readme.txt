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

4. My design is slightly different from the professor's format. Professor created a class named "Parser" to contain
data structures, scanner and parser. I just put them all in the Scanner.py, which was I constructing in Project1, and I
think the idea is similar. According to the project3 description, I used hashmap(dict in py) to store local variables or declarations. 
When the parsing and executing in <decl-seq> was done, the pairs in map would be pushed into stack, 
which stores global variables and map would be clear up. Then it was going to <stmt-seq>. The coding of <Loop> 
and <If> were two tricky parts in the project, as local or new variables might be declared inside the structures. These
narrow scope variables had to be clear once the processing jump out its structure. After the processing
of <Loop> and <If>, my idea is always clearing the current hashmap to empty. 

5. I firstly tested my program in Pycharm, by separately coding execute() functions in the files. After the output
 I tried to use tester.sh  to check the output again in the stdlinux. 
 
   
