import heapq
from collections import deque

class GrafoLogistico:
    def __init__(self):
        # Lista de adjacência: {cidade: [(vizinho, peso), ...]}
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, u, v, peso):
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        # Como o grafo é não-direcionado:
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso))

    def carregar_dados(self, dados_arestas):
        """Monta o grafo a partir de uma lista de tuplas (origem, destino, peso)"""
        for u, v, peso in dados_arestas:
            self.adicionar_aresta(u, v, peso)

    def busca_em_largura(self, inicio):
        """BFS para verificar quais cidades são alcançáveis a partir do início"""
        visitados = set()
        fila = deque([inicio])
        visitados.add(inicio)
        ordem_visita = []

        while fila:
            vertice = fila.popleft()
            ordem_visita.append(vertice)

            for vizinho, _ in self.grafo.get(vertice, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
        
        return ordem_visita

    def dijkstra(self, origem, destino):
        """Encontra a rota com menor quilometragem entre duas cidades"""
        # Inicializa distâncias com infinito
        distancias = {vertice: float('inf') for vertice in self.grafo}
        distancias[origem] = 0
        
        # Guarda o caminho: {filho: pai}
        predecessores = {vertice: None for vertice in self.grafo}
        
        # Fila de prioridade: (distancia, vertice)
        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            dist_atual, vertice_atual = heapq.heappop(fila_prioridade)

            # Se já achamos um caminho menor para ele, desconsidera
            if dist_atual > distancias[vertice_atual]:
                continue

            if vertice_atual == destino:
                break

            for vizinho, peso in self.grafo.get(vertice_atual, []):
                distancia = dist_atual + peso

                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    predecessores[vizinho] = vertice_atual
                    heapq.heappush(fila_prioridade, (distancia, vizinho))

        # Reconstrói o caminho
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = predecessores[atual]
        caminho.reverse()

        return (caminho, distancias[destino])

    def algoritmo_prim(self):
        """Encontra a Árvore Geradora Mínima para conectar toda a rede gastando o mínimo"""
        if not self.grafo:
            return []

        inicio = list(self.grafo.keys())[0]
        visitados = set([inicio])
        arestas_mst = []
        
        # Fila de prioridade para as arestas: (peso, origem, destino)
        fila_arestas = []
        for vizinho, peso in self.grafo[inicio]:
            heapq.heappush(fila_arestas, (peso, inicio, vizinho))

        custo_total = 0

        while fila_arestas:
            peso, u, v = heapq.heappop(fila_arestas)

            if v not in visitados:
                visitados.add(v)
                arestas_mst.append((u, v, peso))
                custo_total += peso

                for proximo_vizinho, novo_peso in self.grafo[v]:
                    if proximo_vizinho not in visitados:
                        heapq.heappush(fila_arestas, (novo_peso, v, proximo_vizinho))

        return arestas_mst, custo_total


# --- Execução do Programa ---
if __name__ == "__main__":
    # Simulação de um arquivo de dados (Entidades e Relações)
    # Formato: (Cidade A, Cidade B, Distância em km)
    dados_logistica = [
        ("São Paulo", "Rio de Janeiro", 430),
        ("São Paulo", "Belo Horizonte", 580),
        ("Rio de Janeiro", "Belo Horizonte", 440),
        ("Belo Horizonte", "Brasília", 730),
        ("São Paulo", "Curitiba", 400),
        ("Curitiba", "Porto Alegre", 710),
        ("Brasília", "Salvador", 1400),
        ("Rio de Janeiro", "Salvador", 1600)
    ]

    # 1. Instanciando e montando o grafo dinamicamente
    sistema_logistico = GrafoLogistico()
    sistema_logistico.carregar_dados(dados_logistica)

    print("=== 1. VERIFICAÇÃO DE CONECTIVIDADE (BFS) ===")
    cidades_alcancaveis = sistema_logistico.busca_em_largura("São Paulo")
    print(f"A partir de São Paulo, é possível alcançar: {', '.join(cidades_alcancaveis)}\n")

    print("=== 2. OTIMIZAÇÃO DE ROTA - CAMINHO MÍNIMO (Dijkstra) ===")
    origem, destino = "Porto Alegre", "Brasília"
    caminho, distancia = sistema_logistico.dijkstra(origem, destino)
    print(f"Melhor rota de {origem} até {destino}: {' -> '.join(caminho)}")
    print(f"Distância total: {distancia} km\n")

    print("=== 3. INFRAESTRUTURA MÍNIMA DE CONEXÃO (Prim) ===")
    mst, custo_infra = sistema_logistico.algoritmo_prim()
    print("Rotas essenciais para conectar todas as cidades com a menor malha possível:")
    for u, v, peso in mst:
        print(f" - {u} <-> {v} ({peso} km)")
    print(f"Extensão total da malha otimizada: {custo_infra} km")