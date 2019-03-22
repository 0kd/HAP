# coding: utf-8


from dijkstra_class import Dijkstra as dc
import counthaps2 as ch


class test:
    def __init__(self,g, hajime, saigo):
        self.g = g
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

for i in range(len(aaa)):
    if int(aaa[i][0][0].split('.')[1]) < int(aaa[i][0][1].split('.')[1]):
        aaa[i] = [aaa[i][0][0], aaa[i][0][1], float(aaa[i][1])]
    else:
        aaa[i] = [aaa[i][0][1], aaa[i][0][0], float(aaa[i][1])]

print(aaa)
bbb = aaa[:]
for i in range(len(aaa)):
    if aaa[i][0].split('counthap')[1] == 'right':
        rev1 = aaa[i][0].split('counthap')[1]+'left'
    else:
        rev1 = aaa[i][0].split('counthap')[1]+'right'
    if aaa[i][1].split('counthap')[1] == 'right':
        rev2 = aaa[i][1].split('counthap')[1]+'left'
    else:
        rev2 = aaa[i][1].split('counthap')[1]+'right'
    rev3 = aaa[i][2]

    for j in range(len(aaa)):
        liss = aaa[i]
        lisj = aaa[j]
        if lisj[0] == rev1 and lisj[j][1] == rev2:
            bbb[i][2] = aaa[i][2]*aaa[j][2]
            bbb[j][2] = aaa[i][2]*aaa[j][2]
        else:
            bbb.append([liss[0], liss[1], liss[2]*lisj[2]])

    print(bbb)

            


# dkao = test(bbb, '10X.1.counthapright', '10X.7842956.counthapright')
dkao = test(aaa, '10X.1.counthapright', '10X.1000.counthapright')
dkao = test(bbb, '10X.1.counthapleft', '10X.1000.counthapright')
dkao = test(bbb, '10X.1.counthapleft', '10X.1000.counthapleft')
# dkao = test(bbb, '10X.1.counthapright', '10X.7842956.counthapleft')
# dkao = test(aaa, '10X.1.counthapleft',  '10X.7842956.counthapright')
# dkao = test(aaa, '10X.1.counthapleft',  '10X.7842956.counthapleft')
# dkao.tracex()









