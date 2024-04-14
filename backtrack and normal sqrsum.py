# Créé par Waîl Yeager, le 14/04/2024 en Python 3.7
def make_graph(n):
    path = []
    graph = [[] for _ in range(n + 1)]
    square_roots = [x**2 for x in range(1, n*2) if x**2 <= n*2]
    for i in range(1, n + 1):
        peers = []
        start = int(i**0.5)
        end = int((n + i)**0.5)
        for j in range(start, end):
            peer = square_roots[j] - i
            if peer != i:
                peers.append(peer)
        graph[i] = peers
    return graph

def chaine_hamiltonienne(graphe, debut, vertices, chemin=[]):
    chemin.append(debut)
    if len(chemin) == vertices:
        return chemin
    for essai in graphe[debut]:
        if essai not in chemin:
            res_path = [i for i in chemin]
            cand = chaine_hamiltonienne(graphe, essai, vertices, res_path)
            if cand:
                return cand
    return None

def square_sums_bis(n):
    graph = make_graph(n)
    for sommet in range(1, n + 1):
        chemin = chaine_hamiltonienne(graph, sommet, n, [])
        if chemin:
            return chemin
    return None

def square_sums(n):
    if n < 15 or (n >= 18 and n < 23) or (n == 24):
        return False

    graph = make_graph(n)
    for i in range(1, n):
        chemin = []
        sommets = list(range(1, n + 1))
        local_graph = [list(graph[x]) for x in range(len(graph))]
        while True:
            sommets.sort(key=lambda x: len(local_graph[x]))
            sommet_actuel = sommets[i]
            i = 0
            chemin.append(sommet_actuel)

            if len(chemin) == n:
                return chemin

            sommet_prochain = local_graph[sommet_actuel]

            for element in sommet_prochain:
                local_graph[element][local_graph[element].index(sommet_actuel)] = local_graph[element][-1]
                local_graph[element].pop()

            if not sommet_prochain and n > 40:
                break
            if not sommet_prochain and n <= 40:
                chemin_hamiltonien = square_sums_bis(n)
                if chemin_hamiltonien:
                    return chemin_hamiltonien

            sommets = sommet_prochain

print(square_sums(40))

