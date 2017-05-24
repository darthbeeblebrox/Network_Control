
# coding: utf-8

# In[2]:

#From:
#   http://stackoverflow.com/questions/37144423/all-possible-maximum-matchings-of-a-bipartite-graph

import networkx as nx
import matplotlib.pyplot as plt

def checkAll(G,m):
    b = nx.bipartite.eppstein_matching(G) # Finds first match
    c = list(b.keys())
    for y in c[int(len(c)/2):]: # Reduces to one occurrence per line
        b.pop(y)
    if len(b) != m: # If new size, break
        return 0
    return b # Add to list of possibilities

def maximal_matching(G):
    edges = G.edges()
    A = []
    m = len(nx.bipartite.eppstein_matching(G))/2 # Create an expected maximum
    for x in range(len(edges)):
        b = checkAll(G,m)
        if b:
            A += [b]
        else:
            break
        keys = list(b.keys())
        cache = (keys[0],b[keys[0]])
        removed = []
        while 1:
            removed += [(keys[1],b[keys[1]])]
            G.remove_edge(keys[1],b[keys[1]]) # Remove first option
            b = checkAll(G,m)
            if b and cache == (keys[0],b[keys[0]]):
                A += [b]
            else:
                break
        G.add_edges_from(removed)
        G.remove_edge(*edges[x])

    return A

def print_matching(A):
    print(list(eval(x) for x in set(str(x) for x in A)))

