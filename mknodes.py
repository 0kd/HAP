import networkx as nx 
import matplotlib.pyplot as plt

G = nx.Graph()

a = "nodes.txt"

ar = open(a)

arr = [ i.split() for i in ar.read().split('\n') if i != '' ]

for i in arr:
    G.add_node(i[0])
    G.add_node(i[1])
    G.add_edge(i[0], i[1])

plt.savefig("test.png")
ar.close()



# [['10X.1011885.counthapright', '10X.1062961.counthapleft', '9.099438423424779e-31'] ....]
