"""
Elabore un programa para un Hospital que determine, y muestre el nivel 
de Leucemia de 803 pacientes clasificando su puntaje si esta inferior 
a 10 no tiene Leucemia; si esta entre 11 y 40, nivel bajo de Leucemia; 
si esta entre 40 y 69, nivel moderado de Leucemia, si esta entre 70 y 
100, nivel grave de Leucemia.
"""


lista_completa = []

def Nivel_leu():
    nombre = input("Ingrese el nombre: ")
    nivel = int(input("Ingrese el puntaje: "))
    clasificacion = ""

    array_niveles =[]
    dicc_niveles = {}

    
    if nivel<10:
        clasificacion = "No tiene  leucemia"
    elif nivel>=11 and nivel<=40:
        clasificacion = "Nivel bajo de leucemia"
    elif nivel>40 and nivel<69:
        clasificacion = "Nivel moderado de lucemia"
    elif nivel>=70 and nivel<=100:
        clasificacion = "Nivel gave de leucemia"
    
    dicc_niveles =  {"nombre: ": nombre, "Nivel: ": nivel, "Clasificacion: ":clasificacion}
    
    array_niveles.append (dicc_niveles)
    
    return array_niveles

for i in range(0,5):

    lista_completa.append(Nivel_leu())

for i in range(0,5):
    print(f"{lista_completa[i]}\n") 