# args: cpounthap

import crit  # return evaluation value. param: left, right, other 
import sys
import crit
import dijkstra as dks
import rev
import counthaps
aaa = counthaps.aaa

groups = []
graph_discarded = []

print(aaa)

class mkkeiro():
    def __init__(self, listg):
        self.listd = listg

        for i in self.listd:
            print(i)

    def numlist(self):  ## return list of number of blocks
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

    evn = liss[2] * aaa[j][2]

    if rec == False:
        bbb[i][2] = evn
        bbb[recj][2] = evn
    else:
        bbb.append([rev1, rev2, evn])
        bbb[i][2] = evn

bbb = sorted(bbb, key=lambda kv: kv[0])

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

        if rec == False:  # 逆が存在
            rece1 = bbb[recj1][2]
            rece2 = bbb[i][2]

            if rece1 > rece2:
                vae = rece2 / rece1
            else:
                vae = rece1 / rece2

            ccc.append([rev1, rev2, vae])
            ccc.append([liss[0], liss[1], vae])
            # 逆の鎖も重み1にして入れる
            # ccc.append([bbb[recj1][0], bbb[recj1][1], 1])
            # ccc.append([bbb[recj1][0], bbb[recj2][1], 1])
        else:  # 逆がない
            ccc.append([rev1, rev2, bbb[i][2]])
            ccc.append([liss[0], liss[1], bbb[i][2]])


ccc1 = ccc[:]
numl = mkkeiro(ccc1).numlist()
print(numl, "ind")
for i in ccc:
    sabun = abs(numl.index(int(i[0].split('.')[1])) - numl.index(int(i[1].split('.')[1])))
    print(i[2])
    i[2] = i[2]/sabun

for i in range(len(ccc)):
    ccc[i] = ((ccc[i][0], ccc[i][1]), ccc[i][2])

for i in range(len(aaa)):
    aaa[i] = ((aaa[i][0], aaa[i][1]), aaa[i][2])
ccc=sorted(ccc, key = lambda kv: kv[1])

print(ccc, "sorted")

for i in ccc:
    count = 0
    change = []

    for j in range(len(groups)):
        for k in groups[j]:
            for l in i[0]:
                # print(k,l)

                if k == l:
                    count = count + 1
                    change.append([int(j),l])
    print(count, "count")

    if count == 0:
        groups.append([i[0][0],i[0][1]])
    elif count == 1:
        groups[change[0][0]].append(i[0][0])
        groups[change[0][0]].append(i[0][1])
        groups[change[0][0]] = list(set(groups[change[0][0]]))
    elif count == 2:
        if len(groups) > 2:
            if ((rev.rev(i[0][0]) in groups[change[0][0]]) and (i[0][1] in groups[change[0][0]])) and ((rev.rev(i[0][1]) in groups[change[0][0]]) and (i[0][0] in groups[change[0][0]])):
                print("break1: ")
                print(i)
                graph_discarded.append(i)
                # break
            else:
                # groups[change[0][0]].append(i[0][0])
                # groups[change[0][0]].append(i[0][1])
                print(change[0], change[1])
                sing = 0

                for e in groups[change[1][0]]:
                    if (rev.rev(e) in groups[change[0][0]]) or (rev.rev(e) in groups[change[0][0]]):
                        # print(i)
                        sing = 1
                        # print("break2")
                        # break

                if sing == 0:
                    if change[0][0] != change[1][0]:
                        for n in groups[change[1][0]]:
                            groups[change[0][0]].append(n)
                        groups.pop(change[1][0])
                    else:
                        pass
                else:
                    print(i)
                    print("break2")
                    graph_discarded.append(i)
                groups[change[0][0]] = list(set(groups[change[0][0]]))
        else:
            if change[0][0] == change[1][0]:
                pass
            else:
                print("fin")
                print(i)

                # break


print(graph_discarded, "discarded")
print("groups:")
#print(groups)

for i in range(len(groups)):
    groups[i]=sorted(groups[i], key = lambda kv: kv.split('.')[1])
    print(groups[i])




