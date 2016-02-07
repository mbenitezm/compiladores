import ply.lex as lex

# Declaracion de tokens
tokens = ( 'PROGRAM', 'IF', 'ELSE', 'VAR', 'PRINT', 'PUNTOCOMA', 'DOSPUNTOS',
           'IGUAL', 'APARENTESIS', 'CPARENTESIS', 'ABRAQUET', 'CBRAQUET',
           'MAYOR', 'MENOR', 'IGUALDAD', 'PUNTO', 'SUMA', 'RESTA', 'MULT',
           'DIV', 'ID', 'INT', 'FLOAT','CTESTRING', 'CTEINT', 'CTEFLOAT' )

#Definicion de tokens
t_ignore = '[\t\n]'
t_PROGRAM  = 'programa'
t_IF = 'if'
t_ELSE = 'else'
t_VAR = 'var'
t_PRINT = 'print'
t_PUNTOCOMA = '\;'
t_DOSPUNTOS = '\:'
t_IGUAL = '\='
t_APARENTESIS = '\('
t_CPARENTESIS = '\)'
t_ABRAQUET = '\{'
t_CBRAQUET = '\}'
t_MAYOR = '\>'
t_MENOR = '\<'
t_IGUALDAD = '\<>'
t_PUNTO = '\.'
t_SUMA = '\+'
t_RESTA = '\-'
t_MULT = '\*'
t_DIV = '\/'
t_INT = 'int'
t_FLOAT = 'float'
t_ID = '[a-zA-Z]+[0-9]*_?[a-zA-Z0-9]+'
t_CTESTRING = '\".*\"     '
t_CTEINT = '[0-9]+ '
t_CTEFLOAT = '[0-9]+\.+[0-9]+'

def t_error(t):
  print "Error de lexer ", t
  exit(-1)
  t.lexer.skip(1)


lexer = lex.lex()