from dijkstra_class import Dijkstra as dc
import counthaps as ch
import rev


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

bbb = aaa[:]

for i in range(len(aaa)):
    liss = aaa[i]
    rev1 = rev.rev(liss[0])
    rev2 = rev.rev(liss[1])
    rev3 = float(liss[2])
    rec = True

    for j in range(len(aaa)):
        lisj = aaa[j]

        if lisj[0] == rev1 and lisj[1] == rev2:
            rec = False
            recj = j

    evn = liss[2]*aaa[j][2]
    if rec == False:
        bbb[i][2] = evn 
        bbb[recj][2] = evn
    else:
        bbb.append([rev1, rev2, evn])
        bbb[i][2] = evn 

bbb=sorted(bbb, key = lambda kv: kv[0])


print(bbb)
            

# 
print("")
dkao = test(bbb, '10X.1.counthapright', '10X.7842956.counthapright')
a = dkao.tracex()
print(a)
# # dkao = test(aaa, '10X.1.counthapright', '10X.1000.counthapright')
# # dkao = test(bbb, '10X.1.counthapleft', '10X.1000.counthapright')
# # dkao = test(bbb, '10X.1.counthapleft', '10X.1000.counthapleft')
print("")
dkao = test(bbb, '10X.1.counthapright', '10X.7842956.counthapleft')
dkao.tracex()
print("")
dkao = test(bbb, '10X.1.counthapleft',  '10X.7842956.counthapright')
dkao.tracex()
print("")
dkao = test(bbb, '10X.1.counthapleft',  '10X.7842956.counthapleft')
dkao.tracex()
# 
# 







