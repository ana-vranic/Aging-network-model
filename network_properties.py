import networkx as nx                                                                                 
import numpy as np

##################################################################### DEGREE DISTRIBUTION ################################
def degree_distribution (edges): #input is np array

    #edges = [(n[0], n[1]) for n in uuw] #make array as list
    G = nx.Graph()
    G.add_edges_from(edges)
    degree_sequence = sorted([int(d) for n, d in G.degree()])

    return np.asarray(degree_sequence)
######################################################## KNN ############################################
def neigh_degree(network, weights):

    d = network.degree()
    nd = nx.average_neighbor_degree(network, weight=weights)
    nodes = network.nodes()

    deg_nd = []

    for n in nodes:
        deg_nd.append((d[n], nd[n]))

    return sorted(deg_nd)

def average_neigh_degree(edges): #import np array

    #edges = [(n[0], n[1]) for n in uuw]
    G = nx.Graph()
    G.add_edges_from(edges)

    return np.asarray(neigh_degree(G, None))
##################################################### CLUSTERING #####################################
def degree_clustering(mreza, tezina):

    d = mreza.degree()
    clustering = nx.clustering(mreza, weight=tezina)
    nodes = mreza.nodes()

    deg_clu = []

    for n in nodes:
        deg_clu.append((d[n], clustering[n]))

    return sorted(deg_clu)

def clustering(edges): #np array

    #edges = [(n[0], n[1]) for n in uuw]
    G = nx.Graph()
    G.add_edges_from(edges)
    d_c = degree_clustering(G, None)

    return np.asarray(d_c)


