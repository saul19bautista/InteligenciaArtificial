def ejecutar():
 def es_par(num):
    return num % 2 == 0

 def suma_de_pares(a, b):
    if es_par(a) and es_par(b):
        suma = a + b
        return True, suma
    return False, 0  

 print("Bienvenidos a la demostración del teorema: la suma de dos números pares es siempre par.")
 numero1 = int(input("Introduce el primer número par: "))
 numero2 = int(input("Introduce el segundo número par: "))

 if es_par(numero1) and es_par(numero2):
    es_suma_par, resultado = suma_de_pares(numero1, numero2)
    if es_suma_par:
        print(f"La suma de {numero1} y {numero2} es: {resultado}, que es un número par.")
    else:
        print(f"Error: la suma de {numero1} y {numero2} no es par.")
 else:
    print("Al menos uno de los números no es par. Asegúrate de ingresar números pares.")
