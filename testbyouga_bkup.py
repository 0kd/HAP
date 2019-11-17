# -*- coding: utf-8 -*-

import networkx as nx
from networkx.readwrite import json_graph
import json
import pylab
import matplotlib.pyplot as plt
import math

G=nx.Graph()

a = open('nodes.txt')
arl = [ i.split() for i in a.read().split('\n') if i!=''  ]
pos = {}
labels = {}

nodes = [ i[0]  for i in arl ] + [ i[1]  for i in arl ]
nodesl = sorted(list(set(nodes)), key=lambda x:int(x.split('.')[1]))
sizes = [10 for i in nodesl]
for i in nodesl:
    G.add_node(i) 
for i in range(len(nodesl)):
    if i%2 == 0:
        pos[nodesl[i]] = (i+1, 0)
    else:
        pos[nodesl[i]] = (i, 0.001)

for i in arl:
    G.add_edge(i[0], i[1])
    # labels[(i[0], i[1])] = str(int(math.log10(float(i[2]))))
    labels[(i[0], i[1])] = str(float(i[2]))



nx.draw(G,pos, node_size = sizes, with_labels = True, font_size = 2,node_color = 'green', edge_color = 'orange' )
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=2, label_pos = 0.4)


plt.savefig("test_fig.png", dpi=1000)
