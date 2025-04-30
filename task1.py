import networkx as nx
import matplotlib.pyplot as plt
from colorama import init, Fore, Style

init(autoreset=True)

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

def analyze_network(G):
    print(f"{Fore.CYAN}{Style.BRIGHT}Назва мережі: {Style.RESET_ALL}{G.name}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}Кількість міст (вузлів): {Style.RESET_ALL}{G.number_of_nodes()}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}Кількість маршрутів (ребер): {Style.RESET_ALL}{G.number_of_edges()}\n")

    print(f"{Fore.GREEN}{Style.BRIGHT}Ступінь вершин (вхідний/вихідний для кожного міста):{Style.RESET_ALL}")
    for city in G.nodes():
        in_deg = G.in_degree(city)
        out_deg = G.out_degree(city)
        color = Fore.MAGENTA if out_deg >= 2 else Fore.WHITE
        print(f"{color}{city}: Вхід: {in_deg}, Вихід: {out_deg}")

def find_shortest_path(G, start, end):
    try:
        length, path = nx.single_source_dijkstra(G, start, target=end, weight='weight')
        print(f"\n{Fore.GREEN}{Style.BRIGHT}Найкоротший шлях від {start} до {end}: {Style.RESET_ALL}{path}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}Час/відстань маршруту: {Style.RESET_ALL}{length} одиниць")
    except nx.NetworkXNoPath:
        print(f"{Fore.RED}Немає доступного маршруту між {start} і {end}.")

def visualize_network(G):
    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G, seed=42) 
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(
        G, pos, with_labels=True, node_color="skyblue", edge_color="gray",
        node_size=2000, font_size=12, font_weight='bold', arrows=True
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Мережа сполучення між польськими містами з напрямками і вагами", fontsize=16)
    plt.savefig("city_transport_network.png")
    plt.show()

analyze_network(G)
visualize_network(G)

find_shortest_path(G, "Warszawa", "Lublin")
find_shortest_path(G, "Gdańsk", "Kraków")
