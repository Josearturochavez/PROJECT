"""
habra un profesor y un asistente
pedir el nombre y edad de los compañeros
ordenar a los compañeros por edad
"""
#obteniendo el numero de alumnos que asistieron
print("ingresa el numero de compañeros que asistieron")
num_companeros = int(input())

#dando instrucciones para ingresar datos al usuario
print("ingresa el nombre del compañero y su edad separados por una linea, repite el proceso con todos los compañeros")

#declarando la lista de compañeros
lista_companeros = []

#introduccion de datos por cada compañero
for i in range(num_companeros):
    nombre = input()
    edad = int(input())
    nuevo_compañero = (nombre,edad)
    lista_companeros.append(nuevo_compañero)

print(lista_companeros)

