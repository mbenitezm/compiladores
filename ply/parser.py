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

def p_e(p):
  '''e: b
   | epsilon'''

def p_bloque(p):
  '''bloque: ABRAQUET f CBRAQUET'''

def p_f(p):
  '''f: estatuto f
   | epsilon'''

def p_estatuto(p):
  '''estatuto: ID IGUAL expresion PUNTOCOMA
          | PRINT APARENTESIS g CPARENTESIS
          | IF APARENTESIS expresion CPARENTESIS bloque i PUNTOCOMA'''

def p_g(p):
  '''g: expresion h
   | CTESTRING h '''

def p_h(p):
  '''h: PUNTOCOMA g
   | epsilon'''

def p_i(p):
  '''i: ELSE bloque
   | epsilon'''

def p_expresion(p):
  '''expresion: exp j'''

def p_j(p):
  '''j: MAYOR exp
   | MENOR exp
   | IGUALDAD exp
   | epsilon'''

def p_exp(p):
  '''exp: terminos k'''

def p_k(p):
  '''k: SUMA exp
   | RESTA
   | epsilon'''

def p_terminos(p):
  '''terminos: factor l'''

def p_l(p):
  '''l: MULT terminos
   | DIV terminos
   | epsilon'''

def p_factor(p):
  '''factor: APARENTESIS expresion CPARENTESIS
        | m varcte'''

def p_m(p):
  '''m: SUMA
   | RESTA
   | epsilon'''

def p_varcte(p):
  '''varcte: ID
        | CTEINT
        | CTEFLOAT'''

def p_epsilon(p):
  '''epsilon:'''

parser = yacc.yacc()