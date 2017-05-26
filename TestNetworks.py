
# coding: utf-8

# In[ ]:

## Returns a networkx digraph of:
#       1-3) One of the three example networks given in Liu 2011 Fig. 1
#         4) The example network given in Wang 2012 Fig .2

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
    elif n == 4:
        G.add_nodes_from(range(1,17))
        G.add_edges_from([(1,16),(16,5),(5,6),(6,7),(7,8),(8,5),(16,9),(9,6),(9,10),(10,11),(11,10),(9,12),(16,13),(13,9),(13,14),(14,15),(15,13),(2,13),(2,3),(2,4)])
        return G
    else:
        print('Bad Input')
        return
    

