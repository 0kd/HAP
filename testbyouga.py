# -*- coding: utf-8 -*-

import networkx as nx
from networkx.readwrite import json_graph
import json
import pylab
import matplotlib.pyplot as plt

# グラフオブジェクトを作成．
G=nx.Graph()

# 頂点を設定する．引数はid．
G.add_node("nodeA")
G.add_node("nodeB")
G.add_node("nodeC")

# 辺を設定する．引数は結びたい頂点．無向グラフなので，順番は気にしない．
G.add_edge("nodeA","nodeB")
G.add_edge("nodeA","nodeC")
G.add_edge("nodeB","nodeC")

# 座標を設定する．indexがid，代入している値が座標．
pos={}
pos["nodeA"]=(0,0)
pos["nodeB"]=(1,1)
pos["nodeC"]=(3,8)

# グラフオブジェクト（点と辺）に座標を関連付けて描画
nx.draw(G,pos)

# 保存
plt.savefig("test_fig.png")

# 表示
