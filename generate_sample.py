from multiprocessing import Pool
import sys
import os
import growing_model as m
import network_properties as netp
import numpy as np
import h5py

def network(N, M, L, a, b,):

    net = m.model(N=N,M=M,L=L,a=a,b=b)
    net = np.asarray(net)
    return net

def map_function(i):
    
    net = network(int(N),M,int(L),float(a),float(b))
    deg_seq = netp.degree_distribution(net)
    #knn = netp.average_neigh_degree(net)
    #clustering = netp.clustering(net)

    return [net, deg_seq,]
    #return [net, deg_seq, knn, clustering]

if __name__ == "__main__":
  
    N = int(sys.argv[1]) #10000
    M = int(sys.argv[2]) #4
    L = int(sys.argv[3]) #4
    a = float(sys.argv[4]) #-1.0
    b = float(sys.argv[5]) #1.8
    j = int(sys.argv[6]) #number of samples
    filename = sys.argv[7]
    
    if os.path.exists(filename):
       print ('file: ', filename, 'exists')
    else:
    
        pool = Pool(4)    
        result = pool.map(map_function, range(int(j)))
   
        with h5py.File(filename, 'w') as F:
            for i,r in enumerate(result):
                F["net_%s"%i] = r[0]
                F["degree_%s"%i] = r[1]
               # F["degree_knn_%s"%i]= r[2]
               # F["degree_clustering_%s"%i] = r[3]
                    
        print ('calculation for:', filename, 'is done')