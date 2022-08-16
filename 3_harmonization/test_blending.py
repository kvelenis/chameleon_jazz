import numpy as np
import os
import json
import pickle
import sys
sys.path.append('..' + os.sep +'0_data_preparation')
import CJ_ChartClasses as ccc

# %% load pickle

with open('../data/all_melody_structs.pickle', 'rb') as handle:
    all_structs = pickle.load(handle)

with open('../data/globalHMM.pickle', 'rb') as handle:
    globalHMM = pickle.load(handle)

# %% load pieces to blend

# i1 will provide the melody and i2 the heaviest transition probabilities
i1, i2 = 0, 10

s1, s2 = all_structs[i1], all_structs[i2]

print(s1.piece_name)
print(s2.piece_name)

# %% construct weighted "blended" transition matrix and get observations

w1, w2, wGlobal = 0.1, 0.8, 0.1

t1 = s1.hmm.transition_matrix.toarray()
t2 = s2.hmm.transition_matrix.toarray()
tGlobal = globalHMM.transition_matrix.toarray()

bt = w1*t1 + w2*t2 + wGlobal*tGlobal

m1 = s1.hmm.melody_per_chord.toarray()