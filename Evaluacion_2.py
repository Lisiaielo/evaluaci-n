class Graph:
    def __init__(self):
        self.vertices = {}  # diccionario para almacenar los vértices y sus conexiones

    def add_vertex(self, vertex, episodes=0):
        if vertex not in self.vertices:
            self.vertices[vertex] = {"episodes": episodes, "connections": {}}

    def add_edge(self, vertex1, vertex2, episodes):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1]["connections"][vertex2] = episodes
            self.vertices[vertex2]["connections"][vertex1] = episodes

    def minimum_spanning_tree(self):
        if not self.vertices:
            return []

        visited = set()
        edges = []
        start_vertex = next(iter(self.vertices))
        visited.add(start_vertex)

        while len(visited) < len(self.vertices):
            min_edge = None
            for vertex in visited:
                for connection, episodes in self.vertices[vertex]["connections"].items():
                    if connection not in visited:
                        if min_edge is None or episodes < min_edge[2]:
                            min_edge = (vertex, connection, episodes)

            if min_edge is None:
                break

            edges.append(min_edge)
            visited.add(min_edge[1])

        return edges

    def contains_yoda(self):
        return "Yoda" in self.vertices

    def max_shared_episodes(self):
        max_episodes = 0
        max_characters = None
        for vertex in self.vertices:
            for connection, episodes in self.vertices[vertex]["connections"].items():
                if episodes > max_episodes:
                    max_episodes = episodes
                    max_characters = (vertex, connection)
        return max_episodes, max_characters


# Crear un grafo y cargar los personajes
star_wars_graph = Graph()

characters = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]
for character in characters:
    star_wars_graph.add_vertex(character)

# Agregar las relaciones entre los personajes
star_wars_graph.add_edge("Luke Skywalker", "Yoda", 3)
star_wars_graph.add_edge("Luke Skywalker", "Darth Vader", 5)

# Impresión de resultados
print("Árbol de expansión mínima:", star_wars_graph.minimum_spanning_tree())
print(f"¿Yoda está en el árbol de expansión mínima? {star_wars_graph.contains_yoda()}")
max_episodes, max_characters = star_wars_graph.max_shared_episodes()
print(f"Número máximo de episodios compartidos: {max_episodes} entre {max_characters[0]} y {max_characters[1]}")