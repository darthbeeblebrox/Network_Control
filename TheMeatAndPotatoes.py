
# coding: utf-8

# In[39]:

from lib import Maximal_ish_matching as mim
from lib import ComputeSMCR as CR
from lib import ComputeCS as CS
from lib import DigraphConvert as DConv
import networkx as nx
import matplotlib.pyplot as plt
import csv
G = nx.read_graphml('elegansGraphML.txt',node_type=int)
nNodes = G.number_of_nodes()
BP = DConv.digraphToBipartite(G)
t = 533 # number of matchings to obtain (533 is the "optimal" value according to Wang's method)
BPMMs = mim.maximal_ish_matching(BP,t,0.05)

# Need to trim off redundancies that come from double-counting output-to-input and input-to-output connections:
BPMMsCut = []
for j in range(len(BPMMs)): #loop over matchings
    BPMMsCut.append({})
    for key in BPMMs[j]:
        if key < nNodes:
            BPMMsCut[j][key] = BPMMs[j][key]
             
MMs = DConv.B2Dmatching(BPMMsCut,nNodes) #convert back to digraph node labelings

# # For nodes not part of a given matching, add them to dict with empty value 
# for matching in MMs:
#     for node in nodeList:
#         if node not in matching:
#             matching[node] = []

# keys = MMs[0].keys()
# with open('people.csv', 'wb') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(toCSV)


# In[40]:

smcr = CR.SMCR(G,MMs)
print('SMCR: ', smcr)

# cs = CS.AllCS(G,MMs)
# print('All CS: ', cs)


# In[31]:

#print(BP.edges())
#print(BPMMsCut)

# dupCheck = []
# redundancies = 0
# for cmm in BPMMsCut:
#     if cmm in dupCheck:
#         redundancies += 1
#     else:
#         dupCheck.append(cmm)
# print('Redundancies: ', redundancies)

nodeList = G.nodes()






# In[20]:

G.number_of_nodes()

