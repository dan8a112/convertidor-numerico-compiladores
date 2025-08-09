# Funciones que permitiran la conversión de numeros a las diferentes bases que manejaremos.

def a_binario(n): return bin(n)[2:]

def a_hexadecimal(n): return hex(n)[2:].upper()

def a_octal(n): return oct(n)[2:].upper()

def a_romano(n):
    val = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = ''
    for (arabic, roman) in val:
        while n >= arabic:
            res += roman
            n -= arabic
    return res

def a_aleatorio(n):
    import random
    opciones = [2, 5, 8, 16, 'romano']
    base = random.choice(opciones)

    if base == 2:
        return f"(base {base}) " + bin(n)[2:]
    elif base == 5:
        return f"(base {base}) " + a_penta(n)
    elif base == 8:
        return f"(base {base}) " + oct(n)[2:]
    elif base == 16:
        return f"(base {base}) " + hex(n)[2:].upper()
    elif base == 'romano':
        return "(base romano) " + a_romano(n)

    
def a_penta(n):
    simbolos = ['ε', 'α', 'β', 'γ', 'δ'] 
    if n == 0:
        return 'ε'
    resultado = ''
    while n > 0:
        resto = n % 5
        resultado = simbolos[resto] + resultado
        n = n // 5
    return resultado

