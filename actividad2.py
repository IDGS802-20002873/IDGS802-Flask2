from flask import Flask,render_template
from flask import request
import formsAct2

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Index():
    len_form = formsActividad.LenguajeForm(request.form)
    val_S = ''
    val_I = ''
    if request.method=='POST' and len_form.validate():
        val_S = len_form.spanish.data
        val_I = len_form.english.data
    
    return render_template("formularioAct2.html",form=num_form,num=num)
        

@app.route("/resultado",methods=["POST"])
def Resultado():
    num = request.form.get("txtNumero")
    num = int(num)
    numMax = 0
    numMin = 0
    numMin = int(request.form.get("numero{}".format(1)))
    numRange = 0
    cont = 0
    suma = 0
    promedio = 0
    lista = []
    listaCom = []

    for i in range(num):
        numRange=int(request.form.get("numero{}".format((i+1))))
        lista.append(numRange)
        if numRange > numMax :
            numMax = numRange
        if numRange < numMin :
            numMin = numRange

    for i in range(num):
        repetido = int(request.form.get("numero{}".format((i+1))))
        contador = lista.count(repetido)
        if(contador > 1):
            listaCom.append("El número {} aparece {} veces.".format(repetido,contador))
    listaRep = list(set(listaCom))
    num = len(listaRep)

    for i in lista:
        suma += i

    promedio = suma/len(lista)

    return render_template("resultadoActividad1.html",num=num,numMax=numMax,numMin=numMin,lista1=listaRep,suma=suma,promedio=promedio)

if __name__ == "__main__":
    app.run(debug=True,port=3000)