from flask import Flask, render_template, request
from logic.lexer import lexical_analyzer
from logic.analyzer import analyze_input
from logic.parser import parser, results
from logic.inputs import split_input

from logic.lark_parser import generar_arbol

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens_list = []
    resultados = []
    lexer_errors = []
    trees = []

    if request.method == 'POST':
        entrada = request.form['entrada']
        lineas = split_input(entrada)
        results.clear()

        tokens_list, lexer_errors = analyze_input(entrada)

        if lexer_errors:
            # Detiene la ejecución, solo muestra los errores léxicos
            resultados.append(("Error léxico", "Corrige los errores léxicos para continuar."))
        else:
            # No hay errores léxicos, continuar parseo
            for linea in lineas:
                trees.append(generar_arbol(lineas[0]))
                try:
                    parser.parse(linea, lexer=lexical_analyzer)
                except Exception as e:
                    resultados.append((linea, f"Error: {e}"))
                    continue

            for r in results:
                numero, tipo, salida = r
                resultados.append((f"{numero}{tipo}$", salida))

    return render_template('index.html',
                           tokens=tokens_list,
                           resultados=resultados,
                           trees=trees,
                           lexer_errors=lexer_errors)

if __name__ == '__main__':
    app.run()
