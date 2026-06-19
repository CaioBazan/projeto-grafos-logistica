# 🚚 Sistema de Otimização de Malha Logística (Teoria dos Grafos)

Este projeto foi desenvolvido como Avaliação Final para a disciplina de Resolução de Problemas Com Grafos. O sistema modela uma rede de transporte intermunicipal (malha rodoviária) utilizando conceitos de grafos estruturados, aplicando algoritmos clássicos para resolver problemas reais de conectividade, rotas mínimas e otimização de infraestrutura.

---

## 📌 Sobre o Domínio e Modelagem

O sistema simula uma rede logística onde:
* Vértices (Nós): Representam as cidades ou centros de distribuição.
* Arestas (Links): Representam as rodovias diretas entre as cidades.
* Tipo de Grafo: Não-direcionado (fluxo bidirecional de ida e volta).
* Pesos: Representam a distância em quilômetros (km) entre os pontos.

### Representação em Memória: Lista de Adjacência
Optou-se pelo uso de uma **Lista de Adjacência** para o armazenamento do grafo. Como redes de transporte reais são grafos *esparsos* (uma cidade não se conecta diretamente a todas as outras), esta abordagem otimiza drasticamente o uso de memória ($O(V + E)$ em comparação ao $O(V^2)$ da matriz) e acelera a busca por vizinhos.

---

## ⚙️ Algoritmos Implementados

1. **Busca em Largura (BFS):** Utilizada para mapear a conectividade da malha a partir de uma origem, garantindo que não existam cidades isoladas no sistema.
2. **Algoritmo de Dijkstra:** Encontra a rota mais curta (menor quilometragem total) entre um ponto de partida e um destino final.
3. **Algoritmo de Prim:** Cria uma Árvore Geradora Mínima (MST), definindo o desenho de infraestrutura ideal para conectar todas as cidades com o menor comprimento de pista possível.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Você precisará apenas do **Python 3.x** instalado em sua máquina. Nenhuma biblioteca externa é necessária (o projeto utiliza apenas estruturas nativas como `heapq` e `collections`).

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/CaioBazan/projeto-grafos-logistica.git](https://github.com/CaioBazan/projeto-grafos-logistica.git)