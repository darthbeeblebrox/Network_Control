
# coding: utf-8

# In[1]:

import networkx as nx

def maximal_ish_matching(G,num_matches=10,tol=0.1):
    '''
    Function that finds approximately maximal matchings by removing nodes and using the built-in networkx function
    
    Input:
        G - undirected, bipartite network
            Note: the nodes should be indexed by integer
        num_matches - number of unique matches to return
        tol - percentage of nodes that can be dropped from the maximal matching 
            (e.g. if tol=0.1, then the returned maximal matchings can be up to 10% smaller than a full maximal matching)
            
    Output:
        all_matches - a list of dictionaries
    '''
    
    #The first matching is easy, and always maximal
    all_matches = []
    all_matches.append(nx.bipartite.hopcroft_karp_matching(G))
    
    #Get the number of nodes corresponding to the tolerance
    tol_num = int((1-tol)*len(all_matches[0]))

    
    #Loop through and remove nodes one by one until we get enough unique matchings
    this_node = min(G.nodes())
    max_node= max(G.nodes())
    
    while True:
        G2 = G.copy()
        G2.remove_node(this_node)
        thismatch = nx.bipartite.hopcroft_karp_matching(G2)
        #Check if this is valid
        if (len(thismatch)>tol_num) and (not thismatch in all_matches):
            all_matches.append(thismatch)
        
        this_node+=1
            
        if len(all_matches)>=num_matches:
            break
        elif this_node>max_node:
            import warnings
            warnings.warn("All nodes cycled through without reaching enough unique cycles; halting and returning all found")
            break
    
    
    return all_matches

