from dijkstra_class import Dijkstra as dc
import counthaps as ch
import rev
aaa = ch.aaa


class test:
    def __init__(self, g, hajime, saigo):
        self.g = g
        self.saigo = saigo
        self.hajime = hajime
        self.memo = 0
        dk = dc(self.g)  # 読み込み
        dk.dump()  # 表示
        self.d, self.fmap = dk.trav(self.hajime)  # Dijkstra法を実行し重みと直前を返す。
        self.lists = []
    def tracex(self):
        if self.fmap[self.saigo] != float('inf'):
            self.trace(self.saigo)

        return self.lists

    def trace(self, saigox):
        # print(saigox, self.d[saigox], self.fmap[saigox],self.fmap,self.g, "trace")

        if ( saigox not in self.d) or  ( saigox not in self.fmap):
            return False

        self.lists.append([saigox, self.d[saigox], self.fmap[saigox]])

        if self.fmap[saigox] != self.hajime:
            self.trace(self.fmap[saigox])
        else:
            return 



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

            break

    evn = liss[2]*aaa[j][2]

    if rec == False:
        bbb[i][2] = evn 
        bbb[recj][2] = evn
    else:
        bbb.append([rev1, rev2, evn])
        bbb[i][2] = evn 

bbb = sorted(bbb, key = lambda kv: kv[0])

ccc = []
visited = []

for i in range(len(bbb)):
    liss = bbb[i]
    rev1 = rev.rev(liss[0])
    rev2 = rev.rev(liss[1])
    rev3 = float(liss[2])
    rec = True
    num1 = liss[0].split('.')[1]
    num2 = liss[1].split('.')[1]

    if [num1, num2] not in visited:
        visited.append([num1, num2])

        for j in range(len(bbb)):
            lisj = bbb[j]

            if lisj[0] == liss[0] and lisj[1] == rev2:
                rec = False
                recj1 = j
            elif lisj[0] == rev1 and lisj[1] == liss[1]:
                recj2 = j
            elif lisj[0] == rev1 and lisj[1] == rev2:
                recj3 = j
        
        if rec == False: # 逆が存在
            rece1 = bbb[recj1][2]
            rece2 = bbb[i][2]

            if rece1 > rece2:
                vae = rece2/rece1
            else:
                vae = rece1/rece2

            ccc.append([rev1, rev2, vae])
            ccc.append([liss[0], liss[1], vae])
            # 逆の鎖も重み1にして入れる
            # ccc.append([bbb[recj1][0], bbb[recj1][1], 1])
            # ccc.append([bbb[recj1][0], bbb[recj2][1], 1])
        else: # 逆がない
            ccc.append([rev1, rev2, bbb[i][2]])
            ccc.append([liss[0], liss[1], bbb[i][2]])





print(bbb)
            
print("ccc")
ccc = sorted(ccc, key = lambda kv: kv[0])
print(ccc)
# 

print("")

## ccc: contradiction was deleted, bbb: contradiction was non-deleted

# print("")
# dkao = test(bbb, '10X.1.counthapright', '10X.7842956.counthapright')
# dkao.tracex()
# print("ccc")
# dkao = test(ccc, '10X.1.counthapright', '10X.7842956.counthapright')
# a = dkao.tracex()
# # dkao = test(aaa, '10X.1.counthapright', '10X.1000.counthapright')
# # dkao = test(bbb, '10X.1.counthapleft', '10X.1000.counthapright')
# # dkao = test(bbb, '10X.1.counthapleft', '10X.1000.counthapleft')
# print("")
# dkao = test(bbb, '10X.1.counthapright', '10X.7842956.counthapleft')
# dkao.tracex()

class mkkeiro(test):
    def __init__(self,listg, startg, endg):
        self.listd = listg
        self.st = startg 
        self.en = endg 
        self.finlis = []

    def numlist(self): ## return list of number of blocks  
        listn = []

        for i in self.listd:
            ii = int(i[0].split('.')[1])

            if ii not in listn:
                listn.append(ii)
            ii = int(i[1].split('.')[1])

            if ii not in listn:
                listn.append(ii)
        listn = sorted(listn)
        # print(listn)

        return listn
    

## make sure listd has beensorted
    def mklist(self, sta, end): # return the part of connection list
        for i in range(len(self.listd)):
            num1 = self.listd[i][0].split('.')[1]
            # print(sta, num1)
            if sta == int(num1):
                stn = i

                break

        enn = -1
        enn1 = -1

        for i in range(len(self.listd)):
            num1 = self.listd[i][0].split('.')[1]

            if end == int(num1):
                enn = i

            if end < int(num1) or i == len(self.listd)-1:
                enn1 = i


#         print(self.listd, stn,end, enn, enn1,  "eeeeeeeeeeeeeeeee")

        if enn != -1:
            list_limited = self.listd[stn:enn+1]
            list_limited2 = []

            for i in list_limited:

                if int(i[0].split('.')[1]) == sta and int(i[1].split('.')[1]) == end:
                    print("removed")
                else:
                    list_limited2.append(i)

            return list_limited2  # [stn:enn+1]
        else:

            return self.listd[stn:enn1+1]

    def keiro_sentaku(self,ccc1, start, end, lista): # return the route
        dkao = test(ccc1, '10X.'+str(start)+'.counthapright', '10X.'+str(end)+'.counthapright')
        a = dkao.tracex()
        dkao = test(ccc1, '10X.'+str(start)+'.counthapright', '10X.'+str(end)+'.counthapleft')
        b = dkao.tracex()

        if a[0][1] > b[0][1]:
            self.keiro(ccc1, '10X.'+str(start)+'.counthapright', '10X.'+str(end)+'.counthapleft', lista)
        else:
            self.keiro(ccc1, '10X.'+str(start)+'.counthapright', '10X.'+str(end)+'.counthapright', lista)
    
    def keiro(self,ccc1, start, end, lista): # return the route
        # dkao = test(ccc1, '10X.'+str(start)+'.counthapright', '10X.'+str(end)+'.counthapright')
        # print(ccc1, '10X.'+str(start)+'.counthapright', '10X.'+str(end)+'.counthapright', "122222222222")
        # a = dkao.tracex()
        # dkao = test(ccc1, '10X.'+str(start)+'.counthapright', '10X.'+str(end)+'.counthapleft')
        # b = dkao.tracex()
        dkao = test(ccc1, start, end)
        b = dkao.tracex()
        if b == False:
            self.finlis.append(b)
            
        print(b, "bbbb")

 #        if a[0][1] > b[0][1]:
        for i in b:
            # print(b, 'bbbbbbbbbb')
            print(i, "iiiiiiiiiiii")
            nummstart = int(i[2].split('.')[1])
            nummend = int(i[0].split('.')[1])

            # if lista.index(nummstart)+1 == lista.index(nummend):

            if len(b) == 1:
                print("if")
                # print(lista.index(nummstart)+1, lista.index(nummend))
                # print(lista, nummstart, nummend)
                self.finlis.append([i[0], i[1], i[2]])

            else:
                print("else")
                # print(lista.index(nummstart)+1, lista.index(nummend))
                # print(lista, nummstart, nummend)
                ddd = self.mklist(nummstart, nummend)

                print(ddd, i[2],nummstart,nummend, "ddddddddddddddddddddddddd")
                if len(ddd) == 2:
                    print("if2")
                    self.finlis.append([i[0], i[1], i[2]])
                else:
                    print("else2")
                    # print(i, "a,b")
                    c = b[:]
                    self.keiro(ddd, i[2], i[0], lista)
#         else:
#             for i in a:
#                 # if lista.index(int(i[2].split('.')[1]))+1 == lista.index(int(i[0].split('.')[1])):
# 
#                 if len(a) == 1:
#                     self.finlis.append([i[0], i[1], i[2]])
# 
#                 else:
#                     ddd = self.mklist(i[2], i[0])
#                     self.keiro(ddd, i[2], i[0])

    def keirox(self):
        listf = self.numlist()
        print(len(self.listd), self.st, self.en)
        self.keiro_sentaku(self.listd, self.st, self.en, listf)

        return self.finlis 

keid = mkkeiro(bbb, 1, 7842956)
print(keid.numlist())
print("mklist")
# print(keid.mklist(5328797, 7842956))
# print(keid.mklist(3860396,5328797))
# print(keid.mklist(1519721 ,6851277))
print(keid.keirox(), "finlis")


# keiro(ccc, 1, 7842956)

# 
# print("")
# dkao = test(ccc, '10X.1.counthapleft',  '10X.7842956.counthapright')
# print("")
#dkao = test(ccc, '10X.1.counthapleft',  '10X.7842956.counthapleft')
# dkao.tracex()
# 
# 












