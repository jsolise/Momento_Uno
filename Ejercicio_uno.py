"""
1)	Elabore un programa para la Universidad de Florida que calcule
los primeros 100 números de la siguiente serie 5, 8, 13, 21, ... 
sin mostrar el 13, y muestre la lista del resultado de los números.
"""

resultado = int(5)
count = int(3)

num1 = int(1)
num2 = int(2)


for i in range(1,100,1):
    
    resultado = num1+num2
    num1 = num2
    num2 = resultado
    if(resultado != 13):
        print(resultado)
    
    