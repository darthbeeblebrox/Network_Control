
# coding: utf-8

# In[ ]:

## Returns a networkx digraph of:
#       1-3) One of the three example networks given in Liu 2011 Fig. 1
#         4) The example network given in Wang 2012 Fig .2

import networkx as nx

def testNet(n):
    G = nx.DiGraph();
    if n == 1:
        G.add_nodes_from(range(4))
        G.add_edges_from([(0,1),(1,2),(2,3)])
        return G
    elif n == 2:
        G.add_nodes_from(range(4))
        G.add_edges_from([(0,1),(0,2),(0,3)])
        return G
    elif n == 3:
        G.add_nodes_from(range(6))
        G.add_edges_from([(0,1),(0,2),(0,3),(0,4),(0,5),(2,3)])
        return G
    elif n == 4:
        G.add_nodes_from(range(16))
        G.add_edges_from([(0,15),(15,4),(4,5),(5,6),(6,7),(7,4),(15,8),(8,5),(8,9),(9,10),(10,9),(8,11),(15,12),(12,8),(12,13),(13,14),(14,12),(1,12),(1,2),(1,3)])
        return G
    elif n == 100:
        G = nx.read_graphml('elegansGraphML.txt',node_type=int)
        return G
    else:
        print('Bad Input; please input an integer from 1-5 or 100 (large C elegans connectome)')
        return
    

