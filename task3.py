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

# Аналіз
def analyze_network(G):
    print(f"{Fore.CYAN}{Style.BRIGHT}Назва мережі:{Style.RESET_ALL} {G.name}")
    print(f"{Fore.YELLOW}Кількість міст: {G.number_of_nodes()}, маршрутів: {G.number_of_edges()}")
    print(f"\n{Fore.GREEN}Ступінь вершин (вхід/вихід):")
    for city in G.nodes():
        print(f" - {city}: Вхід = {G.in_degree(city)}, Вихід = {G.out_degree(city)}")

# Один найкоротший шлях
def find_shortest_path(G, start, end):
    try:
        dist, path = nx.single_source_dijkstra(G, start, end, weight='weight')
        print(f"\n{Fore.BLUE}Шлях з {start} до {end}:{Style.RESET_ALL} {path}")
        print(f"{Fore.MAGENTA}Загальна вага: {dist} од.")
    except nx.NetworkXNoPath:
        print(f"\n{Fore.RED}Немає шляху між {start} і {end}.")

# Таблиця всіх найкоротших відстаней
def shortest_paths_table(G):
    headers = ["Від \\ До"] + cities
    table = []

    for source in cities:
        row = [source]
        lengths, _ = nx.single_source_dijkstra(G, source, weight='weight')
        for target in cities:
            if source == target:
                row.append("—")
            else:
                row.append(lengths.get(target, "∞"))
        table.append(row)

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Таблиця найкоротших відстаней між усіма містами:{Style.RESET_ALL}")
    print(tabulate(table, headers=headers, tablefmt="grid"))

# Запуск
analyze_network(G)
find_shortest_path(G, "Warszawa", "Lublin")
find_shortest_path(G, "Gdańsk", "Kraków")
shortest_paths_table(G)
