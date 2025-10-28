
import heapq

class Grafo:
    def __init__(self):
        self.estacoes = {}

    def adicionar_estacao(self, nome):
        if nome not in self.estacoes:
            self.estacoes[nome] = {}

    def remover_estacao(self, nome):
        if nome in self.estacoes:
            del self.estacoes[nome]
            for conexoes in self.estacoes.values():
                conexoes.pop(nome, None)

    def adicionar_conexao(self, origem, destino, tempo):
        self.adicionar_estacao(origem)
        self.adicionar_estacao(destino)
        self.estacoes[origem][destino] = tempo

    def remover_conexao(self, origem, destino):
        if origem in self.estacoes and destino in self.estacoes[origem]:
            del self.estacoes[origem][destino]

    def consultar_rotas(self, estacao):
        return self.estacoes.get(estacao, {})

    def verificar_conectividade(self, origem, destino, visitado=None):
        if visitado is None:
            visitado = set()
        if origem == destino:
            return True
        visitado.add(origem)
        for vizinho in self.estacoes.get(origem, {}):
            if vizinho not in visitado:
                if self.verificar_conectividade(vizinho, destino, visitado):
                    return True
        return False

    def dijkstra(self, origem, destino):
        fila = [(0, origem, [])]
        visitado = set()

        while fila:
            tempo_atual, estacao_atual, caminho = heapq.heappop(fila)
            if estacao_atual in visitado:
                continue
            caminho = caminho + [estacao_atual]
            if estacao_atual == destino:
                return tempo_atual, caminho
            visitado.add(estacao_atual)
            for vizinho, tempo in self.estacoes.get(estacao_atual, {}).items():
                if vizinho not in visitado:
                    heapq.heappush(fila, (tempo_atual + tempo, vizinho, caminho))
        return float('inf'), []