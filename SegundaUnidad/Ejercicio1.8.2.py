grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]    
}
def heuristica(nodo):
    distancias = {'A':3, 'B':2, 'C':1, 'D':0}
    return distancias.get(nodo, 0)

camino = a_estrella(grafo, 'A','D', heuristica)
print(f"El camino mas corto es: {camino}")


