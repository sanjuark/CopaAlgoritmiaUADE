import csv

# Funciones
def seguir():
    global resp
    respuesta_func = ''
    while respuesta_func.lower() not in resp:
        respuesta_func = input('Desea continuar ingresando datos? Si / No >> ')
    return respuesta_func.lower()

# Variables
headlines_prov = [["Numero de provincia", "Nombre", "Codigo o abreviatura"]]
headlines_part = [["Nombre del partido", "Abreviacion", "Numero de lista"]]
partido_lower,ab_lower,lista= [],[],[]
provincias_lower,abvp_lower = [], []
partidos_generales = []
provincias_totales = []
resp = ['si', 'no']
answer = ''
    
#Pregunta si desea empezar el programa
while answer.lower() not in resp:
    answer = input('Desea empezar el programa? Si / No >> ')
    if answer.lower() not in resp:
        print('Respuesta incorrecta, solo acepto Si / No')


#Etapa 1 (Regiones geograficas) 
while answer.lower() in resp[0]:
    try:
        provincias = int(input("Ingrese la cantidad de provincias actuales en la Argentina, incluyendo la Ciudad Autonoma de Buenos Aires >> "))
    except ValueError: print("El valor debe ser un numero entero")
    for i in range(provincias):
        #Reseteo de variable
        provincia_completa = []
        provincia = f"Provincia {i}"
        provincia_completa.append(provincia)
        while True:
            nombre_provincia = input("Ingrese el nombre de la provincia >> ")
            if nombre_provincia.lower() not in provincias_lower:
                provincia_completa.append(nombre_provincia)
                provincias_lower.append(nombre_provincia.lower())
                break
            else: print("Este nombre de provincia ya fue ingresado")
        while True:
            abv_provincia = input("Ingrese la abreviatura de la provincia >> ")
            if abv_provincia.lower() not in abvp_lower:
                abvp_lower.append(abv_provincia.lower())
                provincia_completa.append(abv_provincia)
                break
            else: print("Esta abreviatura ya fue ingresada")
        provincias_totales.append(provincia_completa)
    break
#Etapa 1 (Partido político)
while answer.lower() in resp[0]:
    #Reseteo de variables
    partido_completo = []
    #Solicitar partido
    while True:
        partido1=input("Ingrese el nombre del partido >> ")
        if partido1.lower() not in partido_lower and partido1 != '':
            partido_lower.append(partido1.lower())
            partido_completo.append(partido1)
            break
        else: print("Este nombre ya fue ingresado o no es posible no ingresar ningun valor")
            
    #Solicitar abreviatura
    while True: 
        abreviatura=input("Ingrese la abreviatura >> ")
        if abreviatura.lower() not in ab_lower:
            ab_lower.append(abreviatura.lower())
            partido_completo.append(abreviatura)
            break
        else: print("Esta abreviatura ya fue ingresada")

    #Solicitar numero de lista
    while True:
        nro_lista=int(input("Ingrese el numero de lista >> "))
        if nro_lista not in lista and nro_lista != 0:
            lista.append(nro_lista)
            partido_completo.append(nro_lista)
            break
        else: print("Este numero de lista ya fue ingresado o no puede ser 0")

    #Agrega el partido a la lista de todos los partidos
    partidos_generales.append(partido_completo)
    
    #Pregunta si desea continuar ingresando datos
    respuesta = seguir()
    if respuesta in resp[1]: break


#Abrir archivos csv y escribir todos los datos
with open ("provincias.csv", "w", newline="") as archivo1:
    writer = csv.writer(archivo1, delimiter=";")
    writer.writerows(headlines_prov)
    writer.writerows(provincias_totales)
archivo1.close()
with open("partidos.csv", 'w', newline='') as archivo2:
    writer = csv.writer(archivo2, delimiter=';')
    writer.writerows(headlines_part)
    writer.writerows(partidos_generales)
archivo2.close()