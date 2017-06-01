
# coding: utf-8

# In[ ]:

import networkx as nx
import matplotlib.pyplot as plt
    
def drawCactus(G,C):
    # draw a cactus (G is full digraph, C is cactus graph)
    # draws cactus in red, rest of G in black
   
    
    # Specify the edges you want here
    red_edges = C.edges()
    edge_colors = ['black' if not edge in red_edges else 'red'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]
    
    node_colors = ['black' if not n in C.nodes() else 'red' for n in G.nodes()]
            

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = node_colors)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
    plt.axis('off')
    plt.show()

