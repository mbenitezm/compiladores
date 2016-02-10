#Marcel Benitez 1139855

# Se importa el lexico
import ply.yacc as yacc
import lexer


tokens = lexer.tokens

#Se declaran las reglan sintacticas
def p_program(p):
  '''program : PROGRAM ID PUNTOCOMA a'''
  print('valid expresion')

def p_a(p):
  '''a : bloque
   | vars bloque'''

def p_vars(p):
  '''vars : VAR b'''

def p_b(p):
  '''b : c d'''

def p_c(p):
  '''c : ID cprima'''

def p_cprima(p):
  '''cprima : COMA c
        | epsilon'''
        
def p_d(p):
  '''d : DOSPUNTOS tipo PUNTOCOMA e'''
   
def p_tipo(p):
  '''tipo : INT
       | FLOAT'''

def p_e(p):
  '''e : b
   | epsilon'''

def p_bloque(p):
  '''bloque : ABRAQUET f CBRAQUET'''

def p_f(p):
  '''f : estatuto f
   | epsilon'''

def p_estatuto(p):
  '''estatuto : ID IGUAL expresion PUNTOCOMA
          | PRINT APARENTESIS g CPARENTESIS PUNTOCOMA
          | IF APARENTESIS expresion CPARENTESIS bloque i PUNTOCOMA'''

def p_g(p):
  '''g : expresion h
   | CTESTRING h '''

def p_h(p):
  '''h : COMA g
   | epsilon'''

def p_i(p):
  '''i : ELSE bloque
   | epsilon'''

def p_expresion(p):
  '''expresion : exp j'''

def p_j(p):
  '''j : MAYOR exp
   | MENOR exp
   | IGUALDAD exp
   | epsilon'''

def p_exp(p):
  '''exp : terminos k'''

def p_k(p):
  '''k : SUMA terminos
   | RESTA terminos
   | epsilon'''

def p_terminos(p):
  '''terminos : factor l'''

def p_l(p):
  '''l : MULT factor
   | DIV factor
   | epsilon'''

def p_factor(p):
  '''factor : APARENTESIS expresion CPARENTESIS
        | m varcte'''

def p_m(p):
  '''m : SUMA
   | RESTA
   | epsilon'''

def p_varcte(p):
  '''varcte : ID
        | CTEINT
        | CTEFLOAT'''

def p_epsilon(p):
  '''epsilon :'''

# Funcion de error
def p_error(p):
  if type(p).__name__ == 'NoneType':
    print('Syntax error')
  else:
    print('Syntax error at token', p.type, p.value)

parser = yacc.yacc()

#Funcion para checar el archivo
def check(filename):
  f = open(filename, 'r')
  data = f.read()
  f.close()
  parser.parse(data)
  