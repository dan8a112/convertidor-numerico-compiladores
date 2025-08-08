# Funciones que permitiran la conversión de numeros a las diferentes bases que manejaremos.

def a_binario(n): return bin(n)[2:]

def a_hexadecimal(n): return hex(n)[2:].upper()

def a_octal(n): return oct(n)[2:]

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
    base = random.randint(2, 16)
    if base == 2:
        return f"(base {base}) " + bin(n)[2:]
    elif base == 8:
        return f"(base {base}) " + oct(n)[2:]
    elif base == 16:
        return f"(base {base}) " + hex(n)[2:].upper()
    else:
        # Conversión manual a base arbitraria
        digits = "0123456789ABCDEF"
        result = ''
        while n > 0:
            result = digits[n % base] + result
            n = n // base
        return f"(base {base}) " + result


