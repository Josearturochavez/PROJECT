def obtener_suplentes():
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

    #se ordenan los compañeros por edad
    lista_companeros.sort(key=lambda x: x[1])
    
    #asigna profesor y asistente y da sus edades
    profesor,profesor_edad = lista_companeros[-1]
    asistente,asistente_edad = lista_companeros[0]

    return profesor,profesor_edad,asistente,asistente_edad

profesor,profesor_edad,asistente,asistente_edad =  obtener_suplentes()
print (f"el profesor es {profesor} con {profesor_edad} años y el asistente es {asistente} con {asistente_edad} años")