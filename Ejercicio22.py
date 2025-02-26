class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Apuntador al siguiente nodo

def ejecutar():
  
    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)

    
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3  

    actual = nodo1
    while actual:
        print(f"[{actual.valor}] ->", end=" ")
        actual = actual.siguiente
    print("None") 

if __name__ == "__main__":
    ejecutar()
