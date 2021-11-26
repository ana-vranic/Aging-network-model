import numpy as np
import random as rn

def norm (i, a, b, g, node):
    sum = 0
    for j in range(1,i):
        node[j]['p']=np.power(node[j]['q'],b)*np.power(g-node[j]['g'],a)
        sum=sum+node[j]['p']
        #print (g, j, node[j]['p'])
    return sum

def probab (i, node, norma):
    prv = []
    for j in range(1,i):
        prv.append (node[j]['p']/norma )   
    return prv
  
    
def init (i, net, node, g):
    node[i]={}
    node[i]['q']=0
    node[i]['p']=0
    node[i]['g']=g
    net[i]=[]

def update (i,j, net, node):

    node[i]['q']+=1
    node[j]['q']+=1
    net[i].append(j)
    net[j].append(i)


def model(N=100,M=1,L=1,a=0.,b=1.):

    """
    N: total number of nodes in the network
    M: number of nodes added at each time step
    L: number of connections that each node make
    a: alpha parameter
    b: beta parameter
    
    return:
    data: adj list of generated network
    """

    node = {}
    net = {}
    g = 1 #time step - generation
    for i in [1, 2]:
        init(i, net, node, g)
        g += 1
    update (1, 2, net, node)

    while i<=L*M:
        #print 'go', g, i
        sum = norm (i, a, b, g, node)

        if i<M: Mo=i   #we add i nodes 
        else: Mo=M
        keys = []
        for k in range(i+1,Mo+i+1):
            init(k, net, node, g)
            keys.append(k)

            ksi=sum*rn.uniform(0,1)
            sum1=0
            for j in range(1, i):
                sum1+=node[j]['p']
                if ksi<=sum1 and (sum1-node[j]['p'])<ksi:
                    if j not in net[k]:
                    #if check(j, keys)==False:
                        update(j,k, net, node)
                        break
                    else:
                        break
        i+= Mo
        g+= 1

    while i<N:
        #print 'g', g, i
        Mo=M
        sum = norm (i, a, b, g, node)
        for k in range(i+1,Mo+i+1): #new nodes
            init(k, net, node, g)
            l=0
            while l<L: #connections
                #print l
                ksi=sum*rn.uniform(0,1)
                sum1=0
                for j in range(1,i): #nodes in existing network
                    sum1=sum1+node[j]['p']
                    if (sum1-node[j]['p'])<ksi and ksi<=sum1:
                        if j not in net[k]:
                            update(j,k, net, node)
                            l+=1
                            break
                        else:
                            break
        i += Mo
        g += 1

    data = []
    for i in range(1,N+1):
        for se in net[i]:
            #print i, se
            data.append((i, se))

    return np.array(data) 


def model_time_series(Mseria=[1, 2, 2, 3], L=1,a =0.,b=1.): #Mseria is vector 

    """
    Mseria is vector: number of nodes added at each time step 
    L: number of connections that each node makes
    a: alpha parameter
    b: beta parameter
    
    return:
    data: adj list of generated network
    """
    
    N = np.sum(Mseria) #number nodes in the network

    node = {}
    net = {}
    g = 0 #time step - generation
    for i in [1, 2]:
        init(i, net, node, g)
        g += 1
    update (1, 2, net, node)
 
    while i<N:
       # print ('g', g, i)
        Mo=Mseria[g-2]
        
        if i<=L: Lo=1
        else: Lo=L 
        sum = norm (i, a, b, g, node)
        
        for k in range(i+1,Mo+i+1): #new nodes
            init(k, net, node, g)
            l=0
            while l<Lo: #connections
                #print l
                ksi=sum*rn.uniform(0,1)
                sum1=0
                for j in range(1,i): #nodes in existing network
                    sum1=sum1+node[j]['p']
                    if (sum1-node[j]['p'])<ksi and ksi<=sum1:
                        if j not in net[k]:
                            update(j,k, net, node)
                            l+=1
                            break
                        else:
                            break
        i += Mo
        g += 1
        
    data = []
    for i in range(1,N+1):
        for se in net[i]:
            #print i, se
            data.append((i, se))
    return data