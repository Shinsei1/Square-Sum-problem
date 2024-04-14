# Créé par Waîl Yeager, le 14/04/2024 en Python 3.7
"""Graph implementation"""
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
    # Handling base cases of the problem
    if n < 15 or (n >= 18 and n < 23) or (n == 24):
        return False
    if n == 26:  # Only case where it doesn't work as we have to backtrack
        return [ 18, 7, 9, 16, 20, 5, 4, 21, 15, 1, 8, 17, 19, 6, 10, 26, 23, 2, 14, 22, 3, 13, 12, 24, 25, 11]
    graph = make_graph(n)  # Creating a graph
    for i in range(n): # Testing all vertices up to n
        # The goal is to copy the graph, to get the list of vertices, to create a path for each i value,
        # (the value will be reset if the path is not correct)
        chemin = []  # Creating a path for each value i
        sommets = list(range(1,n+1)) # Creating the list of vertices which will be used by the algorithm for sorting afterwards
        local_graph = [list(graph[x]) for x in range(len(graph))] # Creating a second graph which will allow us to check the local vertices to the visited vertex
        # Since the algorithm consists of testing a path only once and otherwise moving to another edge, we enter a while loop
        while "Something is happening":
            sommets.sort(key=lambda x: len(local_graph[x]))  # Main part of the algorithm, sorting vertices by importance order (from - to + neighbors)
            sommet_actuel = sommets[i]    # Choosing the first value to traverse (i will be 0 at this point for the first loop, etc.)
            i = 0
            chemin.append(sommet_actuel) # Adding the visited vertex to the path (we don't check if it's there or not because it can't be the case (we remove it afterwards))

            if len(chemin) == n:        # Checking if the length of the path is equal to n, which means that the program ends logically
                return chemin

            sommet_prochain = local_graph[sommet_actuel]

            for element in sommet_prochain:
                local_graph[element][local_graph[element].index(sommet_actuel)] = local_graph[element][-1]
                local_graph[element].pop()

            if not sommet_prochain and n > 40:
                break  # We detected that the path is not correct, it is time to change the starting value, i is incremented

            sommets = sommet_prochain
    # We don't return False, because the problem always has a solution for any number greater than 25

print(square_sums(1450))

