import math as mt

def load_data(file_name):
    data = []
    f = open(file_name, 'r')
    for line in f:
        if not line.startswith('#'):
            data.append(tuple((line.strip().split(' '))))
    f.close()
    return data

def log_binning_dist(base, data): #from raw data = [x....] find logbin data
    data = sorted(data)
    for a in data:
        x0 = a
        if x0!=0:
            break
    Nc = len(data)
    def llim(x):
        j = (mt.log(x) - mt.log(x0))/base
        return x0*mt.exp(base*int(j))
    def ulim(x):
        return llim(x)*mt.exp(base)

    bin_clust = []
    acc = {}
    zero = 0
    for x in data:
        if x!=0:
            key = (llim(x), ulim(x))
            current_avg = acc.get(key, [0,0])
            current_avg[0] += x
            current_avg[1] += 1
            acc[key] = current_avg
        else:
            zero += 1

    for a in acc:
        b = acc[a]
        bin = float(a[1]) - float(a[0])
        bin_clust.append((1.0*b[0]/b[1], 1.0*b[1]/Nc/bin))
    return bin_clust
