from flask import Flask, render_template, request
from logic.lexer import lexical_analyzer
from logic.parser import parser, results
from logic.inputs import split_input

from logic.lark_parser import generar_arbol

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens_list = []
    resultados = []
    arbol = ""

    if request.method == 'POST':
        entrada = request.form['entrada']
        lineas = split_input(entrada)
        results.clear() # Para evitar resultados duplicados de parseos anteriores

        for i, linea in enumerate(lineas):
            lexical_analyzer.input(linea)
            while True:
                tok = lexical_analyzer.token()
                if not tok:
                    break
                tokens_list.append({
                    'line': i + 1,
                    'type': tok.type,
                    'value': tok.value
                })

            try:
                parser.parse(linea, lexer=lexical_analyzer)
            except Exception as e:
                resultados.append((linea, f"Error: {e}"))
                continue

        for r in results:
            numero, tipo, salida = r
            resultados.append((f"{numero}{tipo}$", salida))

            # Generar el árbol sintáctico
        if lineas:
            arbol = generar_arbol(lineas[0])

    return render_template('index.html', tokens=tokens_list, resultados=resultados , arbol=arbol)

if __name__ == '__main__':
    app.run(debug=True)
