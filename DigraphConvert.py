
# coding: utf-8

# In[3]:

import networkx as nx
import matplotlib.pyplot as plt

# # Create Sample Digraph (Fig. 1h from Liu (2011))
# DG = nx.DiGraph()
# DG.add_nodes_from(range(1,7)) #add 6 nodes
# DG.nodes()
# DG.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6),(3,4)])
# #nx.draw(DG, with_labels=True)
# # print('In edges: ')
# # DG.in_edges()
# # print('Out edges: ')
# # DG.out_edges()

def digraphToBipartite(digIn):
    n = digIn.number_of_nodes()
    bipOut = nx.Graph()
    bipOut.add_nodes_from(range(1,2*n+1)) #first n are out nodes, second n are in nodes
    diEdges = digIn.edges()
    for j in diEdges:
        bipOut.add_edge(j[0],j[1]+n) #add edge from output subgraph to input subgraph
    return bipOut

# BP = digraphToBipartite(DG)
# print('Bipartite Output:')
# print(BP.nodes())
# print(BP.edges())

def bipartiteToDigraph(bipIn):
    n = bipIn.number_of_nodes() * 0.5
    if n%1 != 0:
        print('Invalid number of input nodes:')
        print(n)
        return
    n = int(n)
    digOut = nx.DiGraph()
    digOut.add_nodes_from(range(1,n+1))
    bipEdges = bipIn.edges()
    for j in bipEdges:
        digOut.add_edge(j[0],j[1]-n)
    return digOut

# DG_Reconstituted = bipartiteToDigraph(BP)
# print('Digraph Output:')
# print(DG_Reconstituted.nodes())
# print(DG_Reconstituted.edges())

#mm = [{1:6,2:7,3:8},{1:7,4:5,3:8}]

def B2Dmatching(mm,n):
    # mm is a list of dicts of maximal matchings
    # n is the number of nodes in the digraph (i.e. half the number of nodes in the bipartite graph)
    nMM = len(mm) #number of maximal matching configurations
    dgmm = [] #new list to be populated with converted matching dicts
    for k in range(nMM):
        thisMM = mm[k]
        for key in thisMM.keys():
            thisMM[key] = thisMM[key] - n
        dgmm.append(thisMM)
    return dgmm



# In[ ]:



