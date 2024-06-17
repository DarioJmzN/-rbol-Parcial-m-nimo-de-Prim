#Pablo Darío Jiménez Nuño

# Importar las bibliotecas necesarias
import networkx as nx #creación, manipulación y estudio de estructuras, dinámicas y funciones de redes complejas. Permite la creación de grafos (redes) dirigidos y no dirigidos
import matplotlib.pyplot as plt #produce figuras de calidad en una variedad de formatos y entornos interactivos en la plataforma,,, proporciona una interfaz para crear gráficos y figuras en una forma que sea sencilla e intuitiva.
import heapq #proporciona implementaciones basadas en heap de estructuras de datos.

# Definir la función Prim para encontrar el MST
def prim(graph):
    # Inicialización de variables
    start_node = list(graph.nodes())[0]  # Tomar el primer nodo como nodo inicial
    visited = {start_node}  # Conjunto para mantener los nodos visitados
    min_heap = []  # Inicializar el heap como una lista vacía para mantener las aristas
    mst_edges = []  # Lista para almacenar las aristas del MST

    # Función auxiliar para añadir aristas al heap
    def add_edges_to_heap(node):
        for neighbor, attrs in graph.adj[node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (attrs['weight'], node, neighbor))  # Añadir arista al heap con su peso

    # Comenzar desde el primer nodo y añadir sus aristas al heap
    add_edges_to_heap(start_node)

    # Proceso principal de Prim
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)  # Obtener la arista más pequeña del heap
        
        if v not in visited:
            visited.add(v)  # Marcar el nodo como visitado
            mst_edges.append((u, v, {'weight': weight}))  # Añadir la arista al MST
            add_edges_to_heap(v)  # Añadir nuevas aristas desde el nodo recién agregado al MST
    
    return mst_edges  # Devolver las aristas del MST

# Función para visualizar el grafo y el MST
def visualize_graph(graph, mst_edges):
    G = nx.Graph()  # Crear un objeto grafo de NetworkX
    pos = nx.spring_layout(graph)  # Calcular la disposición de los nodos para graficar

    # Añadir nodos al grafo G
    G.add_nodes_from(graph.nodes())

    # Añadir aristas del grafo original con sus pesos
    G.add_edges_from([(u, v, {'weight': d['weight']}) for u, v, d in graph.edges(data=True)])

    # Añadir aristas del MST con color rojo
    G.add_edges_from(mst_edges, edge_color='red')

    # Dibujar el grafo
    edge_colors = [G[u][v]['color'] if 'color' in G[u][v] else 'gray' for u, v in G.edges()]
    edge_labels = {(u, v): f"{G[u][v]['weight']}" for u, v in G.edges()}
    node_labels = {node: f"{node}" for node in G.nodes()}

    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', alpha=0.9)
    nx.draw_networkx_edges(G, pos, width=2.0, edge_color=edge_colors, alpha=0.7)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')
    
    plt.title("Árbol de Expansión Mínima de Prim")
    plt.axis('off')
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Definir un grafo de ejemplo con las clases Casa, Trabajo, Casa, Restaurant, Familia, etc.
    graph = nx.Graph()
    graph.add_weighted_edges_from([
        ('Casa', 'Trabajo', 4), ('Casa', 'Restaurant', 8), ('Trabajo', 'Restaurant', 11), ('Trabajo', 'Amigos', 8),
        ('Restaurant', 'Parque', 7), ('Restaurant', 'Familia', 1), ('Parque', 'Familia', 6), ('Amigos', 'Parque', 2),
        ('Amigos', 'Escuela', 7), ('Amigos', 'canchasBask', 4), ('Familia', 'canchasBask', 2), ('Escuela', 'canchasBask', 14),
        ('Escuela', 'Mercado', 9), ('canchasBask', 'Mercado', 10)
    ])

    # Obtener el árbol de expansión mínima utilizando Prim
    mst_edges = prim(graph)

    # Visualizar el grafo original con el árbol de expansión mínima
    visualize_graph(graph, mst_edges)

