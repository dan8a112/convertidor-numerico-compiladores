import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'NUMERO',
    'TIPO',
    'FIN',
)

# Expresiones regulares para los tokens
t_FIN = r'\$'
t_TIPO = r'(BIN|HEX|DEC|ROM|NEW|ALE)'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)  # Convertir a entero
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexical_analyzer = lex.lex()