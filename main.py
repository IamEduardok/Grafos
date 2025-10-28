import matplotlib.pyplot as plt
import networkx as nx

# Criar grafo direcionado
G = nx.DiGraph()

# Adicionar conexões com tempos
conexoes = [
    ("Estação A", "Estação B", 5),
    ("Estação B", "Estação C", 10),
    ("Estação A", "Estação C", 15),
    ("Estação C", "Estação D", 7),
    ("Estação B", "Estação D", 12),
]

for origem, destino, tempo in conexoes:
    G.add_edge(origem, destino, weight=tempo)

# Layout do grafo
pos = nx.spring_layout(G, seed=42)

# Desenhar nós e arestas
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="#87CEEB")
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color="gray", width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

# tempos nas arestas
labels = nx.get_edge_attributes(G, 'weight')
labels_formatados = {(u, v): f"{tempo} min" for (u, v), tempo in labels.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_formatados, font_size=10)

# Título e ajustes finais
plt.title("Rede de Transporte Público", fontsize=14)
plt.axis("off")
plt.tight_layout()

# Salvar imagem
plt.savefig("rede_transporte_grafo.png")
plt.show()


"""
from grafo import Grafo

rede = Grafo()

rede.adicionar_conexao("Estação A", "Estação B", 5)
rede.adicionar_conexao("Estação B", "Estação C", 10)
rede.adicionar_conexao("Estação A", "Estação C", 15)

print("Rotas de A:", rede.consultar_rotas("Estação A"))
print("Conectividade A → C:", rede.verificar_conectividade("Estação A", "Estação C"))
print("Melhor trajeto A → C:", rede.dijkstra("Estação A", "Estação C"))
"""