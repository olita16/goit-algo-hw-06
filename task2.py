import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.DiGraph(name="City Transport Network")

cities = ["Warszawa", "Gdańsk", "Szczecin", "Wrocław", "Kraków", "Lublin"]
G.add_nodes_from(cities)

connections = [
    ("Warszawa", "Gdańsk", 4),
    ("Gdańsk", "Szczecin", 5),
    ("Szczecin", "Wrocław", 4),
    ("Wrocław", "Kraków", 3),
    ("Kraków", "Lublin", 4),
    ("Lublin", "Warszawa", 2),
]

for city1, city2, weight in connections:
    G.add_edge(city1, city2, weight=weight)

# DFS
def dfs_path(G, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in G:
        return None
    for neighbor in G[start]:
        if neighbor not in path:
            new_path = dfs_path(G, neighbor, end, path)
            if new_path:
                return new_path
    return None

# BFS
def bfs_path(G, start, end):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in G[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# Пошук за допомогою DFS та BFS
start_city = "Warszawa"
end_city = "Lublin"

dfs_result = dfs_path(G, start_city, end_city)
bfs_result = bfs_path(G, start_city, end_city)

print(f"{'DFS Path:':<15} {dfs_result}")
print(f"{'BFS Path:':<15} {bfs_result}")

dfs_result_2 = dfs_path(G, "Gdańsk", "Kraków")
bfs_result_2 = bfs_path(G, "Gdańsk", "Kraków")

print(f"{'DFS Path (Gdańsk -> Kraków):':<30} {dfs_result_2}")
print(f"{'BFS Path (Gdańsk -> Kraków):':<30} {bfs_result_2}")

