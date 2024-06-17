#Pablo Darío Jiménez Nuño

import networkx as nx
import matplotlib.pyplot as plt
import heapq

def prim(graph):
    # Inicialización
    start_node = list(graph.nodes())[0]  # Empezar desde cualquier nodo
    visited = {start_node}
    min_heap = []
    mst_edges = []

    # Función auxiliar para añadir aristas al heap
    def add_edges_to_heap(node):
        for neighbor, attrs in graph.adj[node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (attrs['weight'], node, neighbor))

    # Comenzar desde el primer nodo y añadir sus aristas al heap
    add_edges_to_heap(start_node)

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        
        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, {'weight': weight}))  # Añadir atributos de peso como diccionario
            add_edges_to_heap(v)
    
    return mst_edges

def visualize_graph(graph, mst_edges):
    G = nx.Graph()
    pos = nx.spring_layout(graph)

    # Añadir nodos
    G.add_nodes_from(graph.nodes())

    # Añadir aristas del grafo original
    G.add_edges_from([(u, v, {'weight': d['weight']}) for u, v, d in graph.edges(data=True)])

    # Añadir aristas del MST
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
    
    plt.title("Árbol Parcial mínimo de Prim")
    plt.axis('off')
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Definir un grafo de ejemplo (no dirigido y ponderado)
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
