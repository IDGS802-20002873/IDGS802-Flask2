import ast
'''
f=open('alumnos.txt','r')
nombres = f.read()
print(nombres)

f=open('alumnos.txt','r')
nombres2 = f.readlines()
print(nombres2)
f.close()
'''
'''
palabra = 'Mario'
with open("alumnos.txt",'r') as archivo:
    for linea in archivo:
        if linea == palabra:
            print(linea,end='')
        else:
            print('No se encontro la palabra')
'''
'''
for i in nombres2:
    print(i,end='')
'''
'''
#f=open('colores.txt','a')
alumnos={'Matricula':12345,'Nombre':'Mario','Apellidos':'Lopez','Correo':'alguien@gmail.com'}
try:
    f=open('colores.txt', 'r')
    color = f.readline()
    colorD = eval(color)
    print(colorD)
    while i == 'Red':
        palabra = i
    for i in colorD.keys():
        if i == 'Green':
            palabra = i
        else:
            palabra = ''
    print(palabra)
    #print(colorD['Rojo'])
    #print(colorD['Red'])
    f.close()
except KeyError:
    print("Error: La palabra no existe")
'''
'''
f=open('colores.txt','r')
alumno = f.readline()
f.close()
res=eval(alumno)
print(res)
f1=open('colores.txt','w')
res['Blue']='Azul'
resultado = str(res)
f1.write(resultado)
print(resultado)
f1.close()
'''
#registro = {'Alumno':'Robert'}
#datos = alumno
#valores = alumno.values()
#print(datos['Matricula'])
#print(valores[12345])

#f.write('\nMario')
#f.write('\nPedro')
#f.close()
palabra = 'Red'
word = 'Rojo'
resultado = True
lista = []
f=open('colores.txt', 'r')
color = f.readline()
colorDict = eval(color)
resultado = colorDict[palabra]
for i in colorDict.values():
    lista.append(i)
if word in lista:
    print('El color existe')
f.close()

if resultado == 'Rojo':
    print('El color existe')
else:
    print('El color no existe')
