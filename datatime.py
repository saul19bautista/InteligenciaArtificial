import datetime
def ejecutar():
 nombre = input("Ingresa tu nombre: ")

 fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

 print(f"Nombre del cliente{nombre}! y la fecha y hora {fecha}")