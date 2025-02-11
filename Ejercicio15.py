import datetime
import random

nombreTienda = input("Ingrese el nombre de la tienda: ")
nombreCliente = input("Ingrese su nombre: ")
nombreProducto = input("Ingrese el nombre del producto: ")
totalCompra = float(input("Ingrese el total de la compra: "))

descuento = totalCompra * 0.10 if totalCompra > 100 else 0  
totalAPagar = totalCompra - descuento  

fechaHora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
folio = random.randint(1000, 999999)

print("\n================== 🎰TICKET DE COMPRA 🎰==================")
print(f"Tienda: {nombreTienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fechaHora}")
print("------------------------------------------------------")
print(f"Cliente: {nombreCliente}")
print(f"Producto: {nombreProducto}")
print(f"Total: ${totalCompra:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${totalAPagar:.2f}")
print("------------------------------------------------------")
print("🤪¡Gracias por su compra😝🤪! ¡🤪vuelva pronto!🤪 ")
print("==============================================================")
