import lexer
import ply.yacc as yacc

tokens = lexer.tokens

parser = yacc.yacc()

def p_programa(p):
  '''programa: PROGRAM ID PUNTOCOMA a'''

def p_a(p):
  '''a: bloque
   | vars bloque'''

def p_vars(p):
  '''vars: VAR b'''

def p_b(p):
  '''b: c d'''

def p_c(p):
  '''c: ID cprima'''

def p_cprima(p):
  '''cprima: PUNTO c
        | epsilon'''
        
def p_d(p):
  '''d: DOSPUNTOS tipo PUNTOCOMA e'''
   
def p_tipo(p):
  '''tipo : INT
       | FLOAT'''

  e: b
   | epsilon
   ;

  bloque: ABRAQUET f CBRAQUET
        ;

  f: estatuto f
   | epsilon
   ;

  estatuto: ID IGUAL expresion PUNTOCOMA
          | PRINT APARENTESIS g CPARENTESIS
          | IF APARENTESIS expresion CPARENTESIS bloque i PUNTOCOMA
          ;
  g: expresion h
   | CTESTRING h
   ;

  h: PUNTOCOMA g
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

  k: SUMA exp
   | RESTA
   | epsilon
   ;

  terminos: factor l
          ;

  l: MULT terminos
   | DIV terminos
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

parser = yacc.yacc()