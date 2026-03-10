

frase = input("Ingrese la frase por favor")

vocales = 0 
consonantes = 0

listado_vocales = "aeiou"

for caracter in frase: 
    caracter = caracter.lower()

    if caracter.isalpha(): 
        if caracter in listado_vocales: 
            vocales += 1 
        else: 
            consonantes += 1 

print(f"Vocales: {vocales}, Consonantes: {consonantes}")

#Hablando claro no me esta funcionando el codigo y ya me arreche 