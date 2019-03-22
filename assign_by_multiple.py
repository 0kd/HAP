# args: cpounthap

import crit  # return evaluation value. param: left, right, other 
import sys
import crit
import dijkstra as dks
import rev

hikisuu = sys.argv
con_blo = {}
ookisa = {}
contigs_10X = []
numbers = []

if len(hikisuu)-1 == 0:
    sys.stderr.write("Error: no argument")
else:
    for i in range(len(hikisuu)-1):
        filename=hikisuu[i+1].split("/")[-1].split('_')[-1]
        # filename = hikisuu[i+1]
        # changeg if error
        filenum = int(hikisuu[i+1].split('X')[1].split('.')[1])
        numbers.append(filenum)

        if not (filename in contigs_10X):
            contigs_10X.append(filename)
        f1 = open(hikisuu[i+1])

        for lineline in f1:
            if lineline != '\n':
                linea=lineline.split()
                rname = linea[0]
                qname = linea[1]
                count_left = linea[2]
                count_right = linea[3]
                count_other = linea[4]

                if linea[0] == "rname":
                    pass
                else:
                    if linea[2] == linea[3]:
                        pass
                    elif int(linea[2]) > int(linea[3]):
                        if linea[1] in con_blo:
                            con_blo[linea[1]][filename+"left"] = [linea[2], linea[3], linea[4]]#+"@"+linea[2]+">"+linea[3])
                        else:
                            #con_blo[linea[1]]=[filename+"_left"+" :"+linea[2]+">"+linea[3]]
                            con_blo[linea[1]] = {}
                            con_blo[linea[1]][filename+"left"] = [linea[2], linea[3], linea[4]]
                    elif int(linea[3]) > int(linea[2]):
                        if linea[1] in con_blo:
                            con_blo[linea[1]][filename+"right"] = [linea[2], linea[3], linea[4]]
                        else:
                            #con_blo[linea[1]]=[filename+"_right"+" :"+linea[3]+">"+linea[2]]
                            con_blo[linea[1]] = {}
                            con_blo[linea[1]][filename+"right"] = [linea[2], linea[3], linea[4]]
                    else:
                        sys.stderr.write("There may be strange row")

grapha = {}
for i in con_blo.keys():
    loop = []
    for j in con_blo[i].keys():
        print(j)
        loop.append(j)
        for k in range(len(loop)):
            for l in range(k+1, len(loop)):
                lef = con_blo[i][loop[k]][0]
                rig = con_blo[i][loop[k]][1]
                oth = con_blo[i][loop[k]][2]
                lefr = con_blo[i][loop[l]][0]
                rigr = con_blo[i][loop[l]][1]
                othr = con_blo[i][loop[l]][2]
                evall = crit.keisan(int(lef), int(rig), int(oth))
                evalr = crit.keisan(int(lefr), int(rigr), int(othr))
                if (loop[k], loop[l]) in grapha.keys():
                    grapha[loop[k], loop[l]] = float(grapha[loop[k], loop[l]])*(float(evall) + float(evalr))
                elif (loop[l], loop[k]) in grapha.keys():
                    grapha[loop[l], loop[k]] = float(grapha[loop[l], loop[k]])*(float(evall) + float(evalr))
                    # if float(grapha[loop[k], loop[l]]) < float(evall) + float(evalr):
                    #     pass
                    # else:
                    #     grapha[loop[k], loop[l]] = float(evall) + float(evalr)
                # if (loop[l], loop[k]) in grapha.keys():
                #     if float(grapha[loop[l], loop[k]]) < float(evall) + float(evalr):
                #         pass
                #     else:
                #         grapha[loop[l], loop[k]] = float(evall) + float(evalr)
                else:
                    grapha[loop[k], loop[l]] = float(evall) + float(evalr)

# grapha: {(10X,10X):evalue, ...}



graphas=sorted(grapha.items(), key = lambda kv: kv[1])

print("!!!sorted!!!")
print(graphas)


groups = []
graph_discarded = []


for i in graphas:
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
                break


print(graph_discarded)
print("groups:")
#print(groups)

for i in range(len(groups)):
    groups[i]=sorted(groups[i], key = lambda kv: kv.split('.')[1])
    print(groups[i])

numbers_uni = list(set(numbers))
numbers = numbers_uni
numbers.sort()




def saisyo():
    for i in range(len(numbers)):
        ki1 = 0
        ki2 = 0
        for j in grapha.keys():
            if '10X.'+str(numbers[i])+'.counthapleft' in j:
                ki1 = 1
            if '10X.'+str(numbers[i])+'.counthapright' in j:
                ki2 = 1
            if ki1 == 1 and ki2 ==1:
                return i


def saigo():
    for i in range(len(numbers)):
        ki1 = 0
        ki2 = 0
        for j in grapha.keys():
            if '10X.'+str(numbers[len(numbers)-1-i])+'.counthapleft' in j:
                ki1 = 1
            if '10X.'+str(numbers[len(numbers)-1-i])+'.counthapright' in j:
                ki2 = 1
            if ki1 == 1 and ki2 == 1:
                return len(numbers)-i-1


# '10X'+str(i)+'.counthapleft'
# '10X'+str(i)+'.counthapright'

        
edges = []

for i in grapha.keys():
    edges.append((i[0], i[1], grapha[i]))

# print(edges)






# 
# def dijk(saisyo,saigo):
#     LR = dks.dijkstra(edges,  '10X'+str(numbers[saisyo])+'.counthapleft', '10X'+str(numbers[saigo])+'.counthapright')
#     LL = dks.dijkstra(edges,  '10X'+str(numbers[saisyo])+'.counthapleft', '10X'+str(numbers[saigo]) +'.counthapleft')
#     RR = dks.dijkstra(edges,  '10X'+str(numbers[saisyo])+'.counthapright', '10X'+str(numbers[saigo])+'.counthapright')
#     RL = dks.dijkstra(edges,  '10X'+str(numbers[saisyo])+'.counthapright', '10X'+str(numbers[saigo])+'.counthapleft')
#     return LR, LL, RR, RL
# 
# 	
# print(dijk(saisyo(), saigo()))
# def looping(syo, go):
#     mat = dijk(syo,go)
#     j = mat[0]
#     k = mat[1]
#     l = mat[2]
#     m = mat[3]
#     if j == inf and k == inf:
# 	looping(syo,go-1)
# 	looping(syo+1,go-1)
#     else:
#         if j == inf:
#             return syo,go,k
#         else:
# 	    return syo,go,j
# 
# 
# def looping2(syo, go):
#     mat = dijk(syo,go)
#     j = mat[0]
#     k = mat[1]
#     l = mat[2]
#     m = mat[3]
#     if l == inf and m == inf:
# 	looping(syo,go-1)
# 	looping(syo+1,go-1)
#     else:
#         if l == inf:
#             return syo,go,m
#         else:
# 	    return syo,go,l
# 	
# 	
# 
# 
# if LR[0] > LL[0]:
#     AA = LL   
# elif LR[0] < LL[0]:
#     AA = LR
# 
# if RR[0] > RL[0]:
#     BB = RR
# elif RR[0] < RL[0]:
#     BB = RL
# 
# 
