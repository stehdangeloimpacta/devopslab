from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello Gaby - Stephanie D'Angelo"

if __name__ == '__main__':
    app.run(debug=True)