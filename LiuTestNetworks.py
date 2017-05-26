
# coding: utf-8

# In[ ]:

import networkx as nx

def testNet(n):
    G = nx.DiGraph();
    if n == 1:
        G.add_nodes_from(range(1,5))
        G.add_edges_from([(1,2),(2,3),(3,4)])
        return G
    elif n == 2:
        G.add_nodes_from(range(1,5))
        G.add_edges_from([(1,2),(1,3),(1,4)])
        return G
    elif n == 3:
        G.add_nodes_from(range(1,7))
        G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6),(3,4)])
        return G
    else:
        print('Bad Input')
        return
    

