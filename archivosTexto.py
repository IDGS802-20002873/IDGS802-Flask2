

'''f=open('alumnos.txt','r')
nombres = f.read()
print(nombres)

nombres2 = f.readlines()
print(nombres2)
f.close()

for i in nombres2:
    print(i,end='')'''

f=open('colores.txt','a')
alumno={'Matricula':12345,'Nombre':'Mario','Apellidos':'Lopez','Correo':'alguien@gmail.com'}
registro = ''
for i in alumno:
    print('{}:{}'.format(i,alumno[i]))
    f.write('{}:{}'.format(i,alumno[i]))
#f.write('\nMario')
#f.write('\nPedro')
f.close()
