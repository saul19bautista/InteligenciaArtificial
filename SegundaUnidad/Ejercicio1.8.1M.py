from collections import deque


grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    
    while cola:
        actual = cola.popleft()
        
        if actual not in visitados:
            visitados.add(actual)
            print(actual, end=' ')
            
            for vecino in grafo[actual]:
                if vecino not in visitados:
                    cola.append(vecino)
        
        return visitados

resultado = bfs(grafo, 'A')

print(f"Nodo visitado por BSF", resultado)