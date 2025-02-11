#numero = int(input("Ingrese un numero"))

##if numero > 0:
   # print(f"El numero es mayor {numero}")
#elif numero < 0:
   # print(f"El {numero} es menor a cero")
#else:
 #   print("El numero es cero")

#numero = int(input("Ingrese un número: "))
#numero2 = int(input("Ingrese el segundo número: "))

#if numero > 10 and numero2 < 20:
 #   print("El número es mayor a 10 y menor a 20")
#else:
 #   print("El número no está en ese rango")

#print("El programa ha terminado")
#exelente
#notable
#buena
#suficiente
#na
#nombre 
#materia y la calificacion es
#Ejercicio clases
calificacion = int(input("Ingrese la calificacion: "))
nombre = input("Ingresa tu nombre: ")
materia = input("Ingrese el nombre de la materia: ")

if 95 <= calificacion <= 100:
    print("excelente")
elif 85 <= calificacion <=94:
    print("notable")
elif 75 <= calificacion <=84:
   print("buena")
elif 70 <= calificacion <=74:
        print("suficiente")
elif calificacion <=70:
     print("na")
print(f"Lacalificacion ingresada es: { calificacion } el nombre del alumno es: { nombre } La materia es: { materia }" )