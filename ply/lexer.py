import ply.lex as lex

#Palabras reservadas
reserved = {
   'program' : 'PROGRAM',
   'if' : 'IF',
   'else' : 'ELSE',
   'var' : 'VAR',
   'print' : 'PRINT',
   'int' : 'INT',
   'float' : 'FLOAT'
}

# Declaracion de tokens
tokens = ( 'PROGRAM', 'IF', 'ELSE', 'VAR', 'PRINT','COMA' ,'PUNTOCOMA', 'DOSPUNTOS',
           'IGUAL', 'APARENTESIS', 'CPARENTESIS', 'ABRAQUET', 'CBRAQUET',
           'MAYOR', 'MENOR', 'IGUALDAD', 'PUNTO', 'SUMA', 'RESTA', 'MULT',
           'DIV', 'ID', 'INT', 'FLOAT','CTESTRING', 'CTEINT', 'CTEFLOAT' )

#Definicion de tokens
t_ignore = ' \t\n'
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
t_COMA = '\,'
t_SUMA = '\+'
t_RESTA = '\-'
t_MULT = '\*'
t_DIV = '\/'
t_CTESTRING = '\".*\"     '
t_CTEINT = '[0-9]+ '
t_CTEFLOAT = '[0-9]+\.+[0-9]+'

#Se revisan palabras reservadas
def t_ID(t):
  '[a-zA-Z]+[0-9]*(_[a-zA-Z0-9]+)?'
  t.type = reserved.get(t.value, 'ID')
  return t

#Error en lexico
def t_error(t):
  print "Error de lexer ", t
  exit(-1)
  t.lexer.skip(1)


lexer = lex.lex()