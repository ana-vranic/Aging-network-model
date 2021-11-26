#!/bin/bash

ts_filename="PT_10min_MySpace.data" #number of new users at each time step
L=1 #number of links per node
a=-1.5 #alpha parameter
b=1.5 #beta parameter
i=100 #number of samples
filename="results/${ts_filename}_L${L}_a${a}_b${b}_${i}samples.h5py" #file to save samples

python ./network_models/generate_sample_ts.py  ${ts_filename} ${L} ${a} ${b} ${i} ${filename}


N=1000 #total number of nodes
M=1 #number of nodes per step
L=1 #number of links per node
a=-2.0 #alpha parameter
b=1.5 #beta parameter
i=100 #number of samples
filename="results/N${N}_M${M}_L${L}_a${a}_b${b}_${i}samples.h5py" #file to save samples

#python ./network_models/generate_sample.py  ${N} ${M} ${L} ${a} ${b} ${i} ${filename}