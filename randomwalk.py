# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:53:36 2019

@author: Sucheta
"""

import networkx as nx
import random
import matplotlib.pyplot as pl
import operator

G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
pl.show()
x=random.choice([i for i in range(G.number_of_nodes())])
dict_counter={}
for i in range(G.number_of_nodes()):
    dict_counter[i]=0
    
dict_counter[x]=dict_counter[x]+1
for i in range(1000000000000):
    list_n=list(G.neighbors(x))
    if(len(list_n)==0):
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x]=dict_counter[x]+1
    else:
        random.choice(list_n)
        dict_counter[x]=dict_counter[x]+1
        
p=nx.pagerank(G)
a=sorted(p.items(),key=operator.itemgetter(1))
b=sorted(dict_counter.items(),key=operator.itemgetter(1))

print(a)
print(b)

        

