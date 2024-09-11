"""
5)	Elabore un programa para determinar el funcionamiento optimo 
de las 407 cabinas de metro cable, registrando un puntaje que se 
clasifica de la siguiente forma si tiene 2 puntos está con un 
funcionamiento defectuoso, si tiene 3 puntos el funcionamiento 
es moderado y si tiene 4 puntos el funcionamiento es óptimo.
"""

listado_cabinas = []

def Funcionamiento():
    id_cabina = int(input("Cabina N°: "))
    puntaje = int(input("Puntaje: "))
    estado_cabina = ""

    dicc_cabinas = {}
    array_cabinas = []

    if puntaje == 2:
        estado_cabina = "Funcionamiento defetuoso"
    elif puntaje == 3:
        estado_cabina = "Funcionamiento moderado"
    elif puntaje == 4:
        estado_cabina = "Funcionamiento optimo"
    else:
        estado_cabina = "No determinado"

    dicc_cabinas = {"ID Cabina: ": id_cabina, "Estado: ": estado_cabina}

    array_cabinas.append (dicc_cabinas)

    return array_cabinas

for i in range (0,3):
    listado_cabinas.append (Funcionamiento())

for i in range (0,3):
    print(f"{listado_cabinas[i]}\n")