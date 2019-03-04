
# coding: utf-8

# In[5]:


import heapq
class Dijkstra:
    def __init__(self,g):
        lines = g.split("\n")
        print(lines)
        self.size = int(lines[0]) # 頂点数。ここでは0からself.size-1まで使う。
        self.list = [[] for i in range(self.size)]
        for s in lines[1:]:
            d1,d2,w = s.split(" ")
            self.connect(int(d1),int(d2),int(w)) # 重みも登録する
    def connect(self,x,y,w):
        self.list[x].append([y,w]) # 重みも登録する
    def dump(self):
        for i in range(len(self.list)):
            for u in self.list[i]:
                print(i," ",u[0]," ",u[1])
    def trav(self,s):
        d = [float('inf') for i in range(self.size)] # 距離の配列は最初∞に初期化しておく
        d[s] = 0
        fmap = [None for i in range(self.size)]
        pq = [] # 優先度付き待ち行列
        u = s   # sから始める
        while True:
            for n in self.list[u]: # 隣には (頂点番号、重み) が登録されている
                v,weight = n # vが頂点番号、weightが重み
                if d[v] > d[u]+weight: # uからvに行った方が重みが少なければ、                                
                    d[v] = d[u]+weight # 重みを更新し、
                    heapq.heappush(pq,[d[v],v]) # (重み,頂点番号)を優先度付き待ち行列に登録。重みが小さい順に出てくる
                    fmap[v] = u # 直前の頂点を登録                                        
            if len(pq) == 0: # 空になったらwhileから抜ける
                break
            weight,u = heapq.heappop(pq) # (重みと頂点)を取り出す。
        print(self.list)
        return [d,fmap] # 重みと直前を返す。


# In[6]:


def test():
    g='''5
0 1 10
0 3 5
1 4 1
1 3 2
4 0 7
4 2 6'''
    dk = Dijkstra(g) # 読み込み
    dk.dump()        # 表示
    d,fmap = dk.trav(0) # Dijkstra法を実行し重みと直前を返す。
    for i in range(len(d)):
        print(i,d[i],fmap[i]) # 表示
test()

