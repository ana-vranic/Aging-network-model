from multiprocessing import Pool
import sys
import os
import growing_model as m
import network_properties as netp
import numpy as np
import h5py
import functions as f

def network(time_series, L, a, b,):

    net = m.model_time_series(Mseria=time_series, L=L,a =a,b=b)
    net = np.asarray(net)
    return net

def map_function(i):
    
    net = network(ts, int(L),float(a),float(b))
    deg_seq = netp.degree_distribution(net)
    knn = netp.average_neigh_degree(net)
    clustering = netp.clustering(net)

    return [net, deg_seq, knn, clustering]

if __name__ == "__main__":
  
    ts_file = sys.argv[1]
    L = sys.argv[2] #4
    a = sys.argv[3] #-1.0
    b = sys.argv[4] #1.8
    j = sys.argv[5] #number of samples
    filename = sys.argv[6]
    
    if os.path.exists(filename):
       print ('file: ', filename, 'exists')
    else:
        
        data=f.load_data(ts_file)
        ts = [int(t[1]) for t in data]

        pool = Pool(4)    
        result = pool.map(map_function, range(int(j)))
   
        with h5py.File(filename, 'w') as F:
            for i,r in enumerate(result):
                F["net_%s"%i] = r[0]
                F["degree_%s"%i] = r[1]
                F["degree_knn_%s"%i]= r[2]
                F["degree_clustering_%s"%i] = r[3]
                    
        print ('calculation for:', filename, 'is done')