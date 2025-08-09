from lark import Lark

# Gramática 
grammar = """
    start: expresion
    expresion: NUMERO TIPO FIN

    NUMERO: /[0-9]+/
    TIPO: "BIN" | "HEX" | "DEC" | "ROM" | "ALE"
    FIN: "$"

    %ignore " "
"""

# Crear el parser de Lark
parser = Lark(grammar, start='start')

def generar_arbol(entrada):
    """
    Genera el árbol sintáctico en formato texto bonito para la entrada dada.
    """
    tree = parser.parse(entrada)
    return tree.pretty()

