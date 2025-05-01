import networkx as nx
from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)

# Побудова графа
G = nx.DiGraph(name="City Transport Network")
cities = ["Warszawa", "Gdańsk", "Szczecin", "Wrocław", "Kraków", "Lublin"]
edges = [
    ("Warszawa", "Gdańsk", 4),
    ("Gdańsk", "Szczecin", 5),
    ("Szczecin", "Wrocław", 4),
    ("Wrocław", "Kraków", 3),
    ("Kraków", "Lublin", 4),
    ("Lublin", "Warszawa", 2),
]
G.add_nodes_from(cities)
G.add_weighted_edges_from(edges)

# Функція виводу таблиці на кожному кроці
def print_step_table(distances, visited):
    print("{:<12} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 35)
    for vertex in distances:
        dist = "∞" if distances[vertex] == float("inf") else str(distances[vertex])
        checked = "Так" if vertex in visited else "Ні"
        print("{:<12} {:<10} {:<10}".format(vertex, dist, checked))
    print()

# Реалізація алгоритму Дейкстри з покроковим виводом
def detailed_dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes()}
    distances[start] = 0
    visited = []
    unvisited = list(graph.nodes())

    while unvisited:
        current = min(
            (node for node in unvisited),
            key=lambda node: distances[node],
            default=None
        )

        if current is None or distances[current] == float("inf"):
            break

        for neighbor in graph.neighbors(current):
            weight = graph[current][neighbor]['weight']
            new_distance = distances[current] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        visited.append(current)
        unvisited.remove(current)

        print(f"{Fore.YELLOW}🔍 Оновлення після обробки вершини: {current}")
        print_step_table(distances, visited)

    return distances

# Аналіз мережі
def analyze_network(G):
    print(f"{Fore.CYAN}{Style.BRIGHT}Назва мережі:{Style.RESET_ALL} {G.name}")
    print(f"{Fore.YELLOW}Кількість міст: {G.number_of_nodes()}, маршрутів: {G.number_of_edges()}")
    print(f"\n{Fore.GREEN}Ступінь вершин (вхід/вихід):")
    for city in G.nodes():
        print(f" - {city}: Вхід = {G.in_degree(city)}, Вихід = {G.out_degree(city)}")

# Таблиця всіх найкоротших шляхів з детальною реалізацією
def shortest_paths_table_detailed(G):
    headers = ["Від \\ До"] + cities
    table = []

    for source in cities:
        print(f"{Fore.CYAN}\n=== Алгоритм Дейкстри з покроковим виводом для вершини: {source} ==={Style.RESET_ALL}")
        distances = detailed_dijkstra(G, source)
        row = [source]
        for target in cities:
            if source == target:
                row.append("—")
            else:
                dist = distances.get(target, float("inf"))
                row.append("∞" if dist == float("inf") else dist)
        table.append(row)

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Зведена таблиця найкоротших відстаней (власний алгоритм):{Style.RESET_ALL}")
    print(tabulate(table, headers=headers, tablefmt="grid"))

# --- Запуск ---
analyze_network(G)
shortest_paths_table_detailed(G)
