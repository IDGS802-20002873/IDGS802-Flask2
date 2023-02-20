from flask import Flask,render_template
from flask import request
import formsActividad

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Index():
    num_form=formsActividad.UserForm(request.form)
    num=0
    if request.method=='POST' and (num_form.numero.data!=''):
        num=num_form.numero.data
        num=int(num)
    return render_template("indexActividad1.html",form=num_form,num=num)
        

@app.route("/resultado",methods=["POST"])
def Resultado():
    num = request.form.get("txtNumero")
    num = int(num)
    numMax = 0
    numMin = int(request.form.get("numero {}".format(1)))
    numRange = 0
    lista = []
    lista1 = []
    cont = 0
    suma = 0
    for i in range(num):
        numRange=int(request.form.get("numero {}".format((i+1))))
        lista.append(numRange)
        if numRange>numMax :
            numMax=numRange
        if numRange<numMin :
            numMin=numRange
    for i in range(num):
        numero_repetido = int(request.form.get("numero {}".format((i+1))))
        conteo = lista.count(numero_repetido)
        if(conteo>1) :
            lista1.append("El número {} aparece {} veces.".format(numero_repetido,conteo))
    lista2 = list(set(lista1))
    num=len(lista2)
    for i in lista:
        suma += i
    promedio = suma/len(lista)
    return render_template("resultadoActividad1.html",num=num,numMax=numMax,numMin=numMin,lista1=lista2,suma=suma,promedio=promedio)

if __name__ == "__main__":
    app.run(debug=True,port=3000)