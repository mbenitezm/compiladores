%{
#include <cstdio>
#include <iostream>
using namespace std;

extern "C" int yylex();
extern "C" int yyparse();
extern "C" FILE *yyin;
void yyerror(const char *s);

%}

%start programa
%token PROGRAM
%token IF
%token ELSE
%token VAR
%token PRINT
%token PUNTOCOMA
%token COMA
%token DOSPUNTOS
%token IGUAL
%token APARENTESIS
%token CPARENTESIS
%token ABRAQUET
%token CBRAQUET
%token MAYOR
%token MENOR
%token IGUALDAD
%token PUNTO
%token SUMA
%token RESTA
%token MULT
%token DIV
%token ID
%token INT
%token FLOAT
%token CTESTRING
%token CTEINT
%token CTEFLOAT

%%
  programa: PROGRAM ID PUNTOCOMA a
          ;

  a: bloque
   | vars bloque
   ;

  vars: VAR b
      ;

  b: c d
   ;

  c: ID cprima
   ;

  cprima: COMA c
        | epsilon
        ;

  d: DOSPUNTOS tipo PUNTOCOMA e
   ;

  tipo : INT
       | FLOAT
       ;

  e: b
   | epsilon
   ;

  bloque: ABRAQUET f CBRAQUET
        ;

  f: estatuto f
   | epsilon
   ;

  estatuto: ID IGUAL expresion PUNTOCOMA
          | PRINT APARENTESIS g CPARENTESIS PUNTOCOMA
          | IF APARENTESIS expresion CPARENTESIS PUNTO i PUNTOCOMA
          ;
  g: expresion h
   | CTESTRING h
   ;

  h: COMA g
   | epsilon
   ;

  i: ELSE bloque
   | epsilon
   ;

  expresion: exp j
           ;

  j: MAYOR exp
   | MENOR exp
   | IGUALDAD exp
   | epsilon
   ;

  exp: terminos k
     ;

  k: SUMA terminos
   | RESTA terminos
   | epsilon
   ;

  terminos: factor l
          ;

  l: MULT factor
   | DIV factor
   | epsilon
   ;

  factor: APARENTESIS expresion CPARENTESIS
        | m varcte
        ;

  m: SUMA
   | RESTA
   | epsilon
   ;

  varcte: ID
        | CTEINT
        | CTEFLOAT
        ;

  epsilon:
         ; 

%%


int main (int argc, char *argv[]){
  FILE *archivo = fopen(argv[1], "r");
  if (!archivo){
    cout << "El archivo no se pudo abrir" << endl;
    return -1;
  }
  yyin = archivo;
  do{
    yyparse();
  }while(!feof(yyin));
  cout << "expresión válida" << endl;
}

void yyerror(const char *s) {
  cout << "Syntax error!  Message: " << s << endl;
  exit(-1);
}
