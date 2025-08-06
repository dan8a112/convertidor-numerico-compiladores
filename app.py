from flask import Flask, render_template
from logic.inputs import read_content_txt

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    input = read_content_txt("./inputs/entradas.txt") #Se leen las entradas del archivo
    return render_template("index.html", input=input)

if __name__ == "__main__":
    app.run(debug=True)