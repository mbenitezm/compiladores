%{
#include <iostream>
#include "patito.tab.h"
using namespace std;
#define YY_DECL extern "C" int yylex()
%}


%%
[ \t\n]                                     ;
program                                     return PROGRAM;
if                                          return IF;
else                                        return ELSE;
var                                         return VAR;
print                                       return PRINT;
int                                         return INT;
float                                       return FLOAT;
\;                                          return PUNTOCOMA;
\:                                          return DOSPUNTOS;
\=                                          return IGUAL;
\(                                          return APARENTESIS;
\)                                          return CPARENTESIS;
\{                                          return ABRAQUET;
\}                                          return CBRAQUET;
\>                                          return MAYOR;
\<                                          return MENOR;
\<>                                         return IGUALDAD;
\.                                          return PUNTO;
\,                                          return COMA;
\+                                          return SUMA;
\-                                          return RESTA;
\*                                          return MULT;
\/                                          return DIV;
[a-zA-Z]+[0-9]*(_[a-zA-Z0-9]+)?             return ID;
\".*\"                                      return CTESTRING;
[0-9]+                                      return CTEINT;
[0-9]+\.+[0-9]+                             return CTEFLOAT;
.                                           printf("Lex error in \n%c\n", yytext[0]);


%%

