import networkx as nx 
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
import json
import pylab

G = nx.Graph()

a = "nodes.txt"

ar = open(a)

arr = [i.split() for i in ar.read().split('\n') if i != '']
pos = {}
ilst = []

for i in arr:
    ilst.append(i[0])
    ilst.append(i[1])

ilsta = list(set(ilst))

lisu = sorted(ilsta, key=lambda x:int(x.split('.')[1]))
print(lisu)

for i in range(len(lisu)):
    pos[lisu[i]] = (0, i)
    G.add_node(lisu[i])
    print(lisu[i])

for i in arr:
    G.add_edge(i[0], i[1])
    print(i[0], i[1])


nx.draw(G)
plt.savefig("test.png")
ar.close()



# [['10X.1011885.counthapright', '10X.1062961.counthapleft', '9.099438423424779e-31'] ....]
