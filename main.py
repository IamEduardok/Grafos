
from grafo import Grafo

rede = Grafo()

rede.adicionar_conexao("Estação A", "Estação B", 5)
rede.adicionar_conexao("Estação B", "Estação C", 10)
rede.adicionar_conexao("Estação A", "Estação C", 15)

print("Rotas de A:", rede.consultar_rotas("Estação A"))
print("Conectividade A → C:", rede.verificar_conectividade("Estação A", "Estação C"))
print("Melhor trajeto A → C:", rede.dijkstra("Estação A", "Estação C"))
