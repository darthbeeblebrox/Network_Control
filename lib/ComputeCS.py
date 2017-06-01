
# coding: utf-8

# In[47]:

# Computes the size of the maximum control range (SMCR) for each node in the network
# Inputs are:
#    G, the network digraph
#    AllMM, list of dicts containing all maximum matching configurations
#    m & n, the nodes whose similarity you want to compute (Note that these start from 0)

from lib import BuildCF as CF
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import TestNetworks


def CS(G,AllMM,m,n):
    nodeInds = range(len(G.nodes()))
    MMdigs = [] #list of MM digraphs
    eInd = 0
    for MMdict in AllMM:
        MM = nx.DiGraph()
        MM.add_nodes_from(G.nodes())
        edgeList = []
        for key in MMdict: #convert dict of edges to nx digraph
            edgeList.append([key,MMdict[key]])
        MM.add_edges_from(edgeList)
        MMdigs.append(MM)
    maxSim = 0
    for jCS in range(len(MMdigs)):
        print('MM ', jCS, '/', len(MMdigs))
        MM1 = MMdigs[jCS]
        cacti1 = CF.BuildCF(G,MM1)
        DC1 = CF.downstreamCactus(cacti1,G.nodes()[m])
        for kCS in range(len(MMdigs)):
            MM2 = MMdigs[kCS]
            cacti2 = CF.BuildCF(G,MM2)
            DC2 = CF.downstreamCactus(cacti2,G.nodes()[n])
            sim = len(set(DC1).intersection(DC2))
            if sim > maxSim:
                maxSim = sim
    return maxSim
                
def AllCS(G,AllMM):
    CSims = [ [ 0 for y in range( len(G.nodes()) ) ] for x in range( len(G.nodes()) ) ] # n*n array for storing CR similarities
    nodeInds = range(len(G.nodes()))
    nIter1 = 0
    for m in nodeInds:
        nIter2 = 0
        for n in range(m): #only need n to go up to m-1 because CS is symmetric and diagonals are irrelevant
            print('AllCS: Computing from node ', nIter1, ' to node ', nIter2)
            sim = CS(G,AllMM,m,n)
            CSims[m][n] = sim
            CSims[n][m] = sim
            nIter2 +=1
        nIter1 += 1
    return CSims



# G = TestNetworks.testNet(4)
# AllMM = [{1:16,2:3,5:6,6:7,7:8,8:5,9:12,10:11,11:10,13:14,14:15,15:13,16:9},{1:16,2:4,5:6,6:7,7:8,8:5,9:12,10:11,11:10,13:14,14:15,15:13,16:9}]

# CSmatrix = AllCS(G,AllMM)
# # print(CS(G,AllMM,0,15))

# print(CSmatrix)

# # maxCRs = SMCR(G,AllMM)
# # print(maxCRs)



# In[ ]:



