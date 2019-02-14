# args: cpounthap

import crit  # return evaluation value. param: left, right, other 
import sys
import crit
import dijkstra as dks

hikisuu = sys.argv
con_blo = {}
ookisa = {}
contigs_10X = []
numbers = []

if len(hikisuu)-1 == 0:
    sys.stderr.write("Error: no argument")
else:
    for i in range(len(hikisuu)-1):
        # filename=hikisuu[i+1].split("/")[-1]
        filename = hikisuu[i+1]
        # changeg if error
        filenum = int(hikisuu[i+1].split('X')[1].split('.')[0])
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
                    if int(grapha[loop[k], loop[l]]) < evall + evalr:
                        pass
                    else:
                        grapha[loop[k], loop[l]] = evall + evalr
                else:
                    grapha[loop[k], loop[l]] = evall + evalr
print(grapha)

# grapha: {(10X,10X):evalue, ...}

numbers.sort()


def saisyo():
    for i in range(len(numbers)):
        ki1 = 0
        ki2 = 0
        for j in grapha.keys():
            if '10X'+str(numbers[i])+'.counthapleft' in j:
                ki1 = 1
            if '10X'+str(numbers[i])+'.counthapright' in j:
                ki2 = 1
            if ki1 == 1 and ki2 ==1:
                return i


def saigo():
    for i in range(len(numbers)):
        ki1 = 0
        ki2 = 0
        for j in grapha.keys():
            if '10X'+str(numbers[len(numbers)-1-i])+'.counthapleft' in j:
                ki1 = 1
            if '10X'+str(numbers[len(numbers)-1-i])+'.counthapright' in j:
                ki2 = 1
            if ki1 == 1 and ki2 == 1:
                return len(numbers)-i-1


# '10X'+str(i)+'.counthapleft'
# '10X'+str(i)+'.counthapright'

        
edges = []

for i in grapha.keys():
    edges.append((i[0], i[1], grapha[i]))


LR = dks.dijkstra(edges,  '10X'+str(numbers[saisyo()])+'.counthapleft', '10X'+str(numbers[saigo()])+'.counthapright')
LL = dks.dijkstra(edges,  '10X'+str(numbers[saisyo()])+'.counthapleft', '10X'+str(numbers[saigo()])+'.counthapleft')
RR = dks.dijkstra(edges,  '10X'+str(numbers[saisyo()])+'.counthapright', '10X'+str(numbers[saigo()])+'.counthapright')
RL = dks.dijkstra(edges,  '10X'+str(numbers[saisyo()])+'.counthapright', '10X'+str(numbers[saigo()])+'.counthapleft')

print(LR[0])


if LR[0] > LL[0]:
    AA = LL   
elif LR[0] < LL[0]:
    AA = LR

if RR[0] > RL[0]:
    BB = RR
elif RR[0] < RL[0]:
    BB = RL


print(AA)
