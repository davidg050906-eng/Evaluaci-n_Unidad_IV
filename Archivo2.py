#Ejercico 3
numero = int(input("Ingrese el numero"))

if numero <= 1: 
    print(f"Tu numero es entero")

else: 
    numero_primo = True 

    limite = int(numero ** 0.5) + 1

    for i in range (2, limite):
        if numero % i == 0:
         numero_primo = False
        break 

if numero_primo: 
   print(f"Su numero es primo")
else: 
   print("No es primo, pajuo")