def ejecutar():
 nombre = input("Ingrese su nombre: ")
 nombreProducto = input("Ingrese el nombre del producto: ")
 totalCompra = float(input("Ingrese el total de la compra: "))

 totalAPagar = totalCompra - (totalCompra * 0.10) if totalCompra > 0 else totalCompra

 print(f"¡Felicidades {nombre}!, tienes un descuento del 10% en tu producto {nombreProducto}. El total a pagar es {totalAPagar:.2f}")
