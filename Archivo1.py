#Ejercicio 1
numero = int(input("Ingrese un numero entero positivo"))

if numero < 0:
    print(f"Error, por favor ingresar un numero mayor a 0")
else: 
    suma_numeros = 0 
    temp = numero 

while temp > 0: 
    resultado = temp %10 
    suma_numeros += resultado

    temp = temp // 10 

print(f"El resultado a la suma de los numeros ingresados es: {suma_numeros}")
    
