# Core language compiler
This is a simple compiler for Core langauge, which includes:  
##
Scanner -- the class constructor takes as input the name of the input file and finds the first token (the current token).  
Parser  -- Generate a parse tree for the input Core program using recursive descent & Perform semantic checks on the parse tree.  
Interpreter -- Execute the input program.  
Garbage collection -- reference counting for the values stored on the heap.  

# Grammar  
\<prog> ::= program \<decl-seq> begin \<stmt-seq> end | program begin \<stmt-seq> end  
\<decl-seq> ::= \<decl> | \<decl><decl-seq> | \<func-decl> | \<func-decl>\<decl-seq>  
\<stmt-seq> ::= \<stmt> | \<stmt><stmt-seq>  
\<decl> ::= \<decl-int> | \<decl-class>  
\<decl-int> ::= int \<id-list>;  
\<decl-class> ::= class \<id-list>;  
\<id-list> ::= id | id , \<id-list>  
\<func-decl> ::= id ( class \<formals> ) begin \<stmt-seq> endfunc  
\<formals> ::= id | id , \<formals>  
\<stmt> ::= \<assign> | \<if> | \<loop> | \<in> | \<out> | \<decl> | \<func-call>  
\<func-call> ::= begin id ( \<formals> ) ;  
\<assign> ::= id = \<expr> ; | id = new ; | id = class id ;  
\<in> ::= input id;  
\<out> ::= output \<expr>;  
\<if> ::= if \<cond> then \<stmt-seq> endif  
| if \<cond> then \<stmt-seq> else \<stmt-seq> endif  
\<loop> ::= while \<cond> begin \<stmt-seq> endwhile  
\<cond> ::= \<cmpr> | ! ( \<cond> )  
| <cmpr> or \<cond>  
\<cmpr> ::= \<expr> == \<expr> | \<expr> \< \<expr>  
| \<expr> \<= \<expr>  
\<expr> ::= \<term> | \<term> + \<expr> | \<term> – \<expr>  
\<term> ::= \<factor> | \<factor> * \<term>  
\<factor> ::= id | const | ( \<expr> )  
