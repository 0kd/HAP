from dijkstra_class import Dijkstra as dc
import counthaps as ch


class test:
    def __init__(self,hajime, saigo):
        self.g = '''5
120 1 10
120 3 5
1 2 1
1 3 2
2 4 4
3 1 3
3 2 9
3 4 2
4 120 7
4 2 6'''
        self.saigo = saigo
        self.hajime = hajime
        self.memo = 0
        dk = dc(self.g)  # 読み込み
        dk.dump()  # 表示
        self.d, self.fmap = dk.trav(self.hajime)  # Dijkstra法を実行し重みと直前を返す。
    def tracex(self):
        if self.fmap[self.saigo] != float('inf'):
            self.trace(self.saigo)

    def trace(self, saigox):
        print(saigox, self.d[saigox], self.fmap[saigox])
        if self.fmap[saigox] != self.hajime:
            self.trace(self.fmap[saigox])
        else:
            return

aaa = ch.aaa

dkao = test(120, 4)
dkao.tracex()



