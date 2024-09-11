"""
3)	Elabore un programa para la facultad de Ingeniería que 
pida 400 números e indique si ese número es par o impar; 
me muestre un listado y me indique cuantos son pares y 
cuantos son impares.
"""

num = int(0)
count_par = int(0)
count_impar = int(0)

lista_par = []
lista_impar = []

def f_par_impar(num):
    global  count_par, count_impar

    if (num%2==0):
        count_par = count_par + 1
        lista_par.append(num)
        print(f"El número {num} es par.")
    else:
        count_impar = count_impar + 1
        lista_impar.append(num)
        print(f"El número {num} es impar.")
    
    par_impar = {
        "cant_pares" : count_par,
        "cant_impares" :count_impar,
        "Listato_pares" : lista_par,
        "Listato_impares" : lista_impar,
    }
    
    return par_impar


for i in range(1,401,1):
    num = int(input("Ingrese un número: "))
    resultado = f_par_impar(num)






print(f"Cantidad de números pares: {resultado['cant_pares']}")
print(f"Listado de números pares: {resultado['Listato_pares']}")
print(f"Cantidad de números impares: {resultado['cant_impares']}")
print(f"Listado de números impares: {resultado['Listato_impares']}")


