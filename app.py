from flask import Flask, render_template, Response
from logic.analyzer import analyze_input
from logic.inputs import read_content_txt, split_input

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    input = read_content_txt("./inputs/entradas.txt") #Se leen las entradas del archivo
    toks = analyze_input(input)  #Obtiene los tokens haciendo el analisis lexico

    return render_template("index.html", input=input, tokens=toks)


# Ruta de pruebas (Al final se va  aborrar)
@app.route("/debug", methods=["GET"])
def debug_view():

    print("Pruebas")

    return Response(f"Se ha procesado la prueba", mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)