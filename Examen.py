import Ejercicio1
import Ejercicio2
import Ejercicio3
import Ejercicio4
import Ejercicio5
import Ejercicio6
import Ejercicio7
import Ejercicio8
import Ejercicio9
import Ejercicio10
import PositivoNegativo
import adivinarnum
import Ejercicio13
import datatime
import Ejercicio15
import Tienda
import Ejercicio17
import Ejercicio18
import Ejercicio19
import Ejercicio20

def menu():
    print("\n--- MENÚ DE EJERCICIOS ---")
    print("1.  Ejercicio 1: SUMA")
    print("2.  Ejercicio 2: DATOS ESCOLARES")
    print("3.  Ejercicio 3: DECLARACION DE VARIABLES")
    print("4.  Ejercicio 4: DECLARACION DE VARIABLES + SUMA")
    print("5.  Ejercicio 5: DATOS INGRESAR")
    print("6.  Ejercicio 6: ENTRADA DE DATOS SUMA")
    print("7.  Ejercicio 7: RESTA Y MULTIPLICACION")
    print("8.  Ejercicio 8: RADIO DEL CIRCULO")
    print("9.  Ejercicio 9: PAR O IMPAR")
    print("10. Ejercicio 10: EL NUMERO ES MAYOR A 10")
    print("11. Ejercicio 11: NUMERO POSITIVO O NEGATIVO")
    print("12. Ejercicio 12: ADIVINAR NUMERO")
    print("13. Ejercicio 13: CALIFICACIONES")
    print("14. Ejercicio 14: TIENDA")
    print("15. Ejercicio 15: DESCUENTO 10%")
    print("16. Ejercicio 16: MEJORAR EJERCICIO ANTERIOR")
    print("17. Ejercicio 17: TICKET")
    print("18. Ejercicio 18: DEMOSTRACION DE UN TEOREMA SIMPLE")
    print("19. Ejercicio 19: TEMPERATURA")
    print("20. Ejercicio 20: TEMPERATURA CIUDAD")
    print("21. Salir")

    try:
        opcion = int(input("Elija una opción: "))
        return opcion
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return None

def main():
    while True:
        opcion = menu()
        
        if opcion is None:
            continue
        
        if opcion == 1:
            print("----- Ejercicio 1: SUMAS -----")
            Ejercicio1.ejecutar()  
            print("----------------------------------------------")
        elif opcion == 2:
            print("----- Ejercicio 2: DATOS ESCOLARES -----")
            Ejercicio2.ejecutar()
            print("------------------------------------------------------")
        elif opcion == 3:
            print("----- Ejercicio 3: DECLARACION DE VARIABLES -----")
            Ejercicio3.ejecutar()  
            print("--------------------------------------------")
        elif opcion == 4:
            print("----- Ejercicio 4: DECLARACION DE VARIABLES + SUMA -----")
            Ejercicio4.ejecutar() 
            print("--------------------------------------")
        elif opcion == 5:
            print("----- Ejercicio 5: DATOS INGRESAR -----")
            Ejercicio5.ejecutar()
            print("-----------------------------------------------")
        elif opcion == 6:
            print("----- Ejercicio 6: ENTRADA DE DATOS SUMA -----")
            Ejercicio6.ejecutar()
            print("-----------------------------------------------")
        elif opcion == 7:
            print("----- Ejercicio 7: RESTA Y MULTIPLICACION -----")
            Ejercicio7.ejecutar()
            print("----------------------------------------")
        elif opcion == 8:
            print("----- Ejercicio 8: RADIO DEL CIRCULO -----")
            Ejercicio8.ejecutar()
            print("---------------------------------------------------")
        elif opcion == 9:
            print("----- Ejercicio 9: PAR O IMPAR -----")
            Ejercicio9.ejecutar()
            print("-------------------------------------------------------------------")
        elif opcion == 10:
            print("----- Ejercicio 10: EL NUMERO ES MAYOR A 10 -----")
            Ejercicio10.ejecutar()
            print("------------------------------------------------")
        elif opcion == 11:
            print("----- Ejercicio 11: NUMERO POSITIVO O NEGATIVO -----")
            PositivoNegativo.ejecutar()
            print("----------------------------------------------------")
        elif opcion == 12:
            print("----- Ejercicio 12: ADIVINAR NUMERO -----")
            adivinarnum.ejecutar()
            print("-----------------------------------------------------")
        elif opcion == 13:
            print("----- Ejercicio 13: CALIFICACIONES -----")
            Ejercicio13.ejecutar()
            print("--------------------------------------------------")
        elif opcion == 14:
            print("----- Ejercicio 14: TIENDA -----")
            datatime.ejecutar()
            print("-------------------------------------------------------------")
        elif opcion == 15:
            print("----- Ejercicio 15: DESCUENTO 10% -----")
            Ejercicio15.ejecutar()
            print("-------------------------------------------------")
        elif opcion == 16:
            print("----- Ejercicio 16: MEJORAR EJERCICIO ANTERIOR -----")
            Tienda.ejecutar()
            print("--------------------------------------------------------")
        elif opcion == 17:
            print("----- Ejercicio 17: TICKET -----")
            Ejercicio17.ejecutar()
            print("------------------------------------------------")
        elif opcion == 18:
            print("----- Ejercicio 18: DEMOSTRACION DE UN TEOREMA SIMPLE -----")
            Ejercicio18.ejecutar()
            print("---------------------------------------------------------")
        elif opcion == 19:
            print("----- Ejercicio 19: TEMPERATURA -----")
            Ejercicio19.ejecutar()
            print("-----------------------------------------")
        elif opcion == 20:
            print("----- Ejercicio 20: TEMPERATURA CIUDAD -----")
            Ejercicio20.ejecutar()
            print("------------------------------------------------------------------")
        elif opcion == 21:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
