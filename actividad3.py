from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

import formsAct3

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
csrf=CSRFProtect(app)

@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html')

@app.before_request
def before_request():
    print('numero1')

@app.route("/", methods=["GET", "POST"])
def index():
    form = formsAct3.Resistencias(request.form)
    b1=''
    b2=''
    b3=''
    cb1=''
    cb2=''
    cb3=''
    cbt=''
    lista = []
    tolerancia=0
    resultadox=0
    resultadoFMin=0
    resultadoFMax=0
    succes_message='Cálculo realizado con éxito'
    if request.method == 'POST' and form.validate():
        b1 = form.b1.data
        b2 = form.b2.data
        lista = [b1,b2]
        b3 = form.b3.data
        tolerancia = int(form.tolerancia.data)
        resultado=str(b1+b2)
        resultadox=int(resultado)*int(b3)
        if tolerancia==1:
            resultadoFMin=float(float(resultadox)-float(resultadox)*0.05)
            resultadoFMax=float(float(resultadox)+float(resultadox)*0.05)
        elif tolerancia==0:
            resultadoFMin=float(float(resultadox)-float(resultadox)*0.10)
            resultadoFMax=float(float(resultadox)+float(resultadox)*0.10)    
        flash(succes_message)
        tolerancia=str(tolerancia)
    return render_template("actividad3.html", form = form, lista=lista, itemM=b3, itemT=tolerancia,
                               resultadoFMin=resultadoFMin, resultadox=resultadox, resultadoFMax=resultadoFMax)

@app.after_request
def after_request(response):
    print('numero3')
    return response

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)