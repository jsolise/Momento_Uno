"""
2)	Elabore un programa para el Éxito que determine el salario 
de los 1897 empleados de su compañía, teniendo en cuenta las 
comisiones y la seguridad social que debe pagar, e imprima el 
listado de la información. 
"""
nombre = ""
salario = float(0)
comisiones = float(0)

listaEmpleados = []



def calcular_salario(i, salario, comisiones):
    prestaciones = float(salario * 0.08)
    salario_menos_prest = float(salario - prestaciones)
    neto = salario_menos_prest + comisiones
    array= [i, nombre, salario, comisiones, prestaciones, neto]

    listaEmpleados.append (array)
    return listaEmpleados

    

for i in range(0,2,1):
    nombre = input("Nombre del empleado: ")
    salario = float(input("Salario: "))
    comisiones = float(input("Comisiones: "))
    
    calcular_salario(i, salario, comisiones)
    
for i in range(0,2,1):
    print(f"ID: {listaEmpleados[i][0]} --- nombre: {listaEmpleados[i][1]} --- Salario: {listaEmpleados[i][2]} --- Comisiones: {listaEmpleados[i][3]} --- Prestaciones: {listaEmpleados[i][4]} --- Salario Neto: {listaEmpleados[i][5]}" )