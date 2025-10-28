# 🚇 Rede de Transporte Público (Ônibus/Metrô)

Este projeto simula uma rede de transporte público utilizando grafos em Python. Estações são representadas como vértices e conexões entre elas como arestas com pesos (tempo de trajeto). O sistema permite adicionar/remover estações e conexões, consultar rotas, verificar conectividade e calcular o trajeto mais rápido entre dois pontos.

---

## 📦 Funcionalidades

- Adicionar e remover estações
- Adicionar e remover conexões com tempo de trajeto
- Consultar rotas disponíveis a partir de uma estação
- Verificar se é possível chegar de uma estação a outra
- Calcular o trajeto mais rápido usando o algoritmo de Dijkstra
- Gerar uma imagem visual do grafo com as conexões e tempos

---

## 🖼️ Visualização do Grafo

O script `grafo_visual.py` gera uma imagem chamada `rede_transporte_grafo.png` com:

- Estações como nós
- Conexões como setas direcionais
- Tempos de trajeto exibidos nas arestas

---

## ▶️ Como Executar

1. **Instale o Python** (se ainda não tiver instalado)

2. **Instale as bibliotecas necessárias**:

```bash
py -m pip install matplotlib networkx
```

3.  **Execute o script principal**:

 ```bash
 py main.py
 ```


 


