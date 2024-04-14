#In this file , im using a function to backtrack when the path is not good, as it is not the right way to solve this problem (solution is becoming slower at n = 50), im using it only on low values(<=40)
#it is also a way for not having to get the result of 26 to put it in 
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
    return False 

def square_sums(n):
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

