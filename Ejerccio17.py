
temperatura = int(input("Ingresa la temperatura entre 16 -17, 30-31, 26-27, 20-21 para conocer su ciudad: "))

if 16 <= temperatura <= 17:
    print(f"temperatura  Tlaxiaco es de: {temperatura} C")

elif 30 <= temperatura  < 31:
    print(f"La temperatura en la ciudad es putla es de: {temperatura} C")

elif 26 <= temperatura < 27:
    print(f"La temperatura en la ciudad es mexico es de {temperatura} C")

elif 20 <= temperatura < 21:
    print(f"La temperatura en la ciudad de Santa fe es de {temperatura} C")

else:
    print("no hay datos de esas ciudad")

