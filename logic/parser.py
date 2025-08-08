import ply.yacc as yacc
from logic.lexer import tokens
from logic.conversions import *

# Lista para que podamos guardar los resultados
results = []

# Reglas gramaticales
def p_expresion(p):
    '''expresion : NUMERO TIPO FIN'''
    numero = p[1]
    tipo = p[2]

    if tipo == "BIN":
        resultado = a_binario(numero)
    elif tipo == "HEX":
        resultado = a_hexadecimal(numero)
    elif tipo == "DEC":
        resultado = str(numero)
    elif tipo == "ROM":
        resultado = a_romano(numero)
    elif tipo == "ALE":
        resultado = a_aleatorio(numero)
    else:
        resultado = "Tipo no reconocido"

    results.append((numero, tipo, resultado))
    p[0] = resultado

# Aquí podremos manejar todos los errores 
def p_error(p):
    if p:
        print(f"Error de sintaxis en: {p.value}")
    else:
        print("Error de sintaxis al final de la entrada")

# Crear el parser
parser = yacc.yacc()
