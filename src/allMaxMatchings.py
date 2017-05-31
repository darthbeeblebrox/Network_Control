import networkx as nx
import matplotlib.pyplot as plt

#%matplotlib inline

#myg = nx.read_gml('elegansGML.gml.txt')
#G = nx.read_adjlist('elegansAdj.csv')
G = nx.read_adjlist('LiuEx2_Adj.csv')


elarge=[(u,v) for (u,v,d) in G.edges(data=True) if 1]


pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=10)

# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=0.1)
#nx.draw_networkx_edges(G,pos,edgelist=esmall,
#                    width=6,alpha=0.5,edge_color='b',style='dashed')

# labels
#nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png

print('starting matching')

#print(nx.maximal_matching(G))
# Maximum Matching Algorithm
# stolen from stackoverflow: https://stackoverflow.com/questions/37144423/all-possible-maximum-matchings-of-a-bipartite-graphnx.draw(G, with_labels=True)

def checkAll(G,m):
    b = nx.bipartite.eppstein_matching(G) # Finds first match
    c = list(b.keys())
    for y in c[int(len(c)/2):]: # Reduces to one occurrence per line
        b.pop(y)
    if len(b) != m: # If new size, break
        return 0
    return b # Add to list of possibilities
	
edges = G.edges()
A = []
m = len(nx.bipartite.eppstein_matching(G))/2 # Create an expected maximum
for x in range(len(edges)):
    b = checkAll(G,m)
    print(b)
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
        #keys = list(b.keys())
        print(b)
        print(keys)
        if b and cache == (keys[0],b[keys[0]]):
            A += [b]
        else:
            break
    G.add_edges_from(removed)
    G.remove_edge(*edges[x])
print(list(eval(x) for x in set(str(x) for x in A)))

plt.show()

print('done')