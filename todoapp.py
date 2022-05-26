#importar la libreria flask
from flask import Flask, redirect, request, render_template, url_for
import pickle
app = Flask(__name__, template_folder='templates')

datosF = []

@app.route('/')
#contenedor para llamar a index.html y los datos registrados en la ruta principal
def index():
    #pickle_in = open("dict.pickle","rb")
   # dict = pickle.load(pickle_in)
    return render_template('/index.html', datosF=datosF)

#ejecutar
if __name__ == '__main__':
    app.run(debug=True)