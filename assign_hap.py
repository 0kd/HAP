import sys
import crit
import itertools
import math

argn= len(sys.argv)
pbl = {}

if argn == 1:
    print('Error: no argument', file=sys.stderr)
else:
    for i in range(argn-1):
        with open(sys.argv[i+1]) as counthap:
            name10x = sys.argv[i+1].split('.')[1]
            line = counthap.readline().split()
            while line:
                if line[0] == 'rname':
                    line = counthap.readline().split()
                else:
                    pbname = line[1]
                    if pbname not in pbl:
                        pbl[pbname] = {}
                    wrongrate = crit.keisan(int(line[3]), int(line[2]), int(line[4]))
                    if int(line[3]) > int(line[2]):
                        pbl[pbname][name10x+'.right'] = wrongrate
                    if int(line[3]) < int(line[2]):
                        pbl[pbname][name10x+'.left'] = wrongrate
    
                    line = counthap.readline().split()
    
valued = {}
for i in pbl.keys():
    for j in list(itertools.combinations(pbl[i].keys(), 2)):
        values = math.log10(pbl[i][j[0]]) + math.log10(pbl[i][j[1]])
        if j not in valued:
            valued[j] = [values]
        else:
            valued[j].append(math.log10(pbl[i][j[0]]) + math.log10(pbl[i][j[1]]))

valuec = {}
for i in valued:
    valuec[i] = sum(valued[i])
    
for i in valuec:
    print('10X.'+i[0], '10X.'+i[1], valuec[i])

