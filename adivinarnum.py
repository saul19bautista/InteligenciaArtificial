import random 

numero_aleatorio = random.randint(1, 10)
adivina = int(input("Adidivina el numero entre 1, 10: "))

print(f"El numero aleatorio es {numero_aleatorio}.")
if adivina == numero_aleatorio :
    print("Felicidades, adivinaste el numero!")
else:
    print("Lo siento, no adivinaste el numero.")