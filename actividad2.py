from flask import Flask,render_template
from flask import request
import formsAct2

app=Flask(__name__)

def validar(val_S, val_I):
    listaSpanish = []
    listaEnglish = [] 
    # validacion de las palabras
    f=open('colores.txt', 'r')
    color = f.readline()
    colorDict = eval(color)
    f.close()

    for i in colorDict.keys():
        listaEnglish.append(i)
    for j in colorDict.values():
        listaSpanish.append(j)  
        
    if val_S in listaSpanish:
        return True
    elif val_I in listaEnglish:
        return True
    else:
        return False

@app.route("/",methods=["GET","POST"])
def Index():
    len_form = formsAct2.LenguajeForm(request.form)
    accion = ''
    val_I = ''
    val_S = ''
    bol = False
    if request.method=='POST':
        val_S=len_form.spanish.data
        val_I=len_form.english.data
        bol = validar(val_S, val_I)
    if bol == True:
        f1=open('colores.txt','r')
        colores = f1.readline()
        f1.close()
        resultado=eval(colores)
        f2=open('colores.txt','w')
        resultado[val_I]=val_S
        resultado = str(resultado)
        f2.write(resultado)
        f2.close()
        accion = 'Palabras guardadas con exito'  
    return render_template("formularioAct2.html",form=len_form, val_I=val_I)
    


@app.route("/resultado",methods=["POST"])
def Resultado():
    palabra = ''
    len_form = formsAct2.LenguajeForm(request.form)
    if request.method=='POST' and len_form.validate():
        palabra = len_form.search.data
        opcion = int(request.form.get("btnOpcion"))
        if opcion == 1:
            with open('SpanishColors.txt') as archivo:
                datosArchivo = archivo.readlines()
                for i in datosArchivo:
                    if palabra in i:
                        palabra = i
                    else:
                        palabra = 'La palabra no existe en el diccionario'
        elif opcion == 0:
            with open('EnglishColors.txt') as archivo:
                datosArchivo = archivo.readlines()
                for i in datosArchivo:
                    if palabra in i:
                        palabra = i
                    else:
                        palabra = 'La palabra no existe en el diccionario'
    return render_template("formularioAct2.html",form=len_form,buscar=palabra)

if __name__ == "__main__":
    app.run(debug=True,port=3000)