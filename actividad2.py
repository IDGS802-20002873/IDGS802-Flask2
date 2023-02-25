from flask import Flask,render_template
from flask import request
import formsAct2

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Index():
    len_form = formsAct2.LenguajeForm(request.form)
    s=''
    i=''
    if request.method=='POST':
        s=len_form.spanish.data
        i=len_form.english.data
    return render_template("formularioAct2.html",form=len_form, i=i, s=s)
    
@app.route("/guardar",methods=["POST"])
def Diccionario():
    len_form = formsAct2.LenguajeForm(request.form)
    listaSpanish = []
    listaEnglish = []
    accion = ''
    val_S=''
    val_I=''
    if request.method=='POST':
        
        f=open('colores.txt', 'r')
        color = f.readline()
        colorDict = eval(color)
        f.close()

        for i in colorDict.keys():
            listaEnglish.append(i)

        for j in colorDict.values():
            listaSpanish.append(j) 

        val_S=str(len_form.spanish.data)
        val_I=str(len_form.english.data)
        val_S=val_S.upper()
        val_I=val_I.upper()

        if val_S in listaSpanish: 
            accion = 'La palabra ya existe en el diccionario, intenta con otra'
        if val_I in listaEnglish:   
            accion = 'La palabra ya existe en el diccionario, intenta con otra'
        else:
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
    return render_template("formularioAct2.html",form=len_form, res=accion)


@app.route("/resultado",methods=["POST"])
def Resultado():
    len_form = formsAct2.LenguajeForm(request.form)
    palabra = ''
    listaSpanish = []
    listaEnglish = []
    buscador = ''
    if request.method=='POST':
        opcion = int(request.form.get("btnOpcion"))
        if opcion == 1:
            f=open('colores.txt', 'r')
            color = f.readline()
            colorDict = eval(color)
            f.close()

            for i in colorDict.keys():
                listaEnglish.append(i)

            for j in colorDict.values():
                listaSpanish.append(j)

            palabra=str(len_form.search.data)
            palabra=palabra.upper()

            if palabra in listaEnglish: 
                buscador=colorDict[palabra]
            elif palabra in listaSpanish:   
                buscador = palabra
            else:
                buscador = 'El color no existe en el diccionario'
        elif opcion == 0:
            f=open('colores.txt', 'r')
            color = f.readline()
            colorDict = eval(color)
            f.close()

            for i in colorDict.keys():
                listaEnglish.append(i)

            for j in colorDict.values():
                listaSpanish.append(j) 
            
            palabra=str(len_form.search.data)
            palabra=palabra.upper()

            if palabra in listaEnglish: 
                buscador = palabra
            elif palabra in listaSpanish:   
                for key, value in colorDict.items():
                    if palabra == value:
                        buscador = key
            else:
                buscador = 'El color no existe en el diccionario'
    return render_template("formularioAct2.html",form=len_form,buscar=buscador)

if __name__ == "__main__":
    app.run(debug=True,port=3000)