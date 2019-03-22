# coding: utf-8

import heapq


class Dijkstra:
    def __init__(self,g):
        lines = g
        # self.size = int(lines[0]) # 頂点数。ここでは0からself.size-1まで使う。
        self.list = {} # [[] for i in range(self.size)]
        self.arrr = []
        for s in lines:
            d1,d2,w = s
            self.arrr.append(d1)
            self.arrr.append(d2)
        self.arrr = list(set(self.arrr))
        for s in self.arrr:
            self.list[s] = []
        # print(self.list)
        for s in lines:
            d1,d2,w = s
            self.connect(d1,d2,float(w)) # 重みも登録する
    def connect(self,x,y,w):
        self.list[x].append([y,w]) # 重みも登録する
    def dump(self):
            print(self.list)
    def trav(self,s):
        d = {}
        for j in self.arrr:
            d[j] = float('inf')  # 距離の配列は最初∞に初期化しておく
        d[s] = 0
        fmap = {} # [None for i in range(self.size)]
        for j in self.arrr:
            fmap[j] = None  # 距離の配列は最初∞に初期化しておく
        pq = [] # 優先度付き待ち行列
        u = s   # sから始める
        while True:
            if u in self.list:
                for n in self.list[u]: # 隣には (頂点番号、重み) が登録されている
                    v,weight = n # vが頂点番号、weightが重み
                    print(u, v, weight)
                    if d[v] > d[u]+weight: # uからvに行った方が重みが少なければ、                                
                        d[v] = d[u]+weight # 重みを更新し、
                        heapq.heappush(pq,[d[v],v]) # (重み,頂点番号)を優先度付き待ち行列に登録。重みが小さい順に出てくる
                        fmap[v] = u # 直前の頂点を登録                                        
                if len(pq) == 0: # 空になったらwhileから抜ける
                    break
                weight,u = heapq.heappop(pq) # (重みと頂点)を取り出す。
        return [d,fmap] # 重みと直前を返す。

