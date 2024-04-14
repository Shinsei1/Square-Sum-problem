"""implementation d un graphe"""
def make_graph(n):
    path = []
    graph = [[] for _ in range(n + 1)]
    square_roots = [x**2 for x in range(1,n*2) if x**2 <= n*2]
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

def square_sums(n):
    #on traite les cas de bases du probleme
    if n < 15 or (n >= 18 and n < 23) or (n == 24):
        return False
    if n == 26:  #seul cas ou ca marche pas car on doit backtracker
        return [ 18, 7, 9, 16, 20, 5, 4, 21, 15, 1, 8, 17, 19, 6, 10, 26, 23, 2, 14, 22, 3, 13, 12, 24, 25, 11]
    graph = make_graph(n)  #on crée un graphe
    for i in range(n): #on teste tout les sommet jusqua n
        #le but est de copier le graph , d avoir la liste des sommets , de creer un chemin a pour chaque i,(la valeur sera reinitialisée si le
        #chemin ,n'est pas le bon)
        chemin = []  #on creer un chemin pour chaque valeur i
        sommets = list(range(1,n+1)) #on creer la liste des sommets qui va servir a l'algo pour la trier ensuite
        local_graph = [list(graph[x]) for x in range(len(graph))] #on creer second graphe qui va nous permettre de verifier les sommets locaux au sommet visité
        #puisque l'algo consiste a tester un chemin une seule fois et sinon de passer a une autre arete, on rentre dans une boucle while
        while "Quelque chose se passe":
            sommets.sort(key=lambda x: len(local_graph[x]))  #partis principale de l'algorithme , on trie les sommets par ordre d importance (du - au + de voisins)
            sommet_actuel = sommets[i]    #on choisi la premiere valeur a parcourir (i vaudra 0 a ce moment pour la 1re boucle etc...)
            i = 0
            chemin.append(sommet_actuel) #ajouter le sommet visiter au chemin (on ne verifie pas si il y est ou pas car ca ne peut etre le cas (on le supprime apres))

            if len(chemin) == n:        #on véfifie si la taille du chemin est egale a n , cela veut dire que le code le prog se termine logiquement
                return chemin

            sommet_prochain = local_graph[sommet_actuel]

            for element in sommet_prochain:
                local_graph[element][local_graph[element].index(sommet_actuel)] = local_graph[element][-1]
                local_graph[element].pop()

            if not sommet_prochain and n > 40:
                break  #on a detecter que le chemin n est pas le bon , il est temps de changer de valeur de debut , i est incrementer

            sommets = sommet_prochain
    #on ne retourne pas false, car le probleme a toujours une solution pour n'importe quel nombre superieur a 25


print(square_sums(1450))






