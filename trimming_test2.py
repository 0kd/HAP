import glob
import os
import sys

sonzai = 0

d = {}
for i in glob.glob('*.show') :
    a = open(i)
    for i in range(6):
        b = a.readline()
        if i == 0:
            nu1 = b.split()[0]
            nu2 = b.split()[1]

    nu1f = open(nu1)
    klk1 = nu1f.read().split('\n')
    lll1 = int(len(klk1[1]))
    nu1f.close()

    nu2f = open(nu2)
    klk2 = nu2f.read().split('\n')
    lll2 = int(len(klk2[1]))
    nu2f.close()

    print(nu1, nu2, lll1, lll2, "lll")
    doo = 0
    while b:
        c = b.split()
        # if int(c[0]) < 2000 and int(c[6]) > 1000 and float(c[9]) > 80:
        if  int(c[0]) < 200 or lll2 - int(c[4]) < 200  :
            print( lll2 - int(c[4]))
            if int(c[6]) > 2000: # and float(c[9]) > 80:
                sonzai = 1
                doo = 1
                if  int(c[0]) > lll2 - int(c[4])  : # int(c[6]) > int(c[7]):
                    cutnu = nu2
                    start = int(c[3])
                    goal = int(c[4])
                else:
                    cutnu = nu1
                    start = int(c[0])
                    goal = int(c[1])
                if cutnu in d:
                    d[cutnu].append(sorted([start, goal]))
                else:
                    d[cutnu] = []
                    d[cutnu].append(sorted([start, goal]))
            # break
#         if int(c[3]) < 5000 or lll1 - int(c[1]) < 5000 :
#             if int(c[6]) > 5000 and float(c[9]) > 80:
#                 sonzai = 1
#                 doo = 1
#                 if  int(c[3]) < lll1 - int(c[1])  : # int(c[6]) > int(c[7]):
#                     cutnu = nu2
#                     start = int(c[3])
#                     goal = int(c[4])
#                 else:
#                     cutnu = nu1
#                     start = int(c[0])
#                     goal = int(c[1])
#                 if cutnu in d:
#                     d[cutnu].append(sorted([start, goal]))
#                 else:
#                     d[cutnu] = []
#                     d[cutnu].append(sorted([start, goal]))
            
        b = a.readline()
    # if doo = 0:
    #     os.system('mv '+i+' '+i+'.fin')
          
    a.close()
if sonzai == 0:
    os.system('rm  fin')
# print(d)
for i in d:
    d[i] = sorted(d[i], key = lambda kv: int(kv[0]))

print("Located by nucmer:")
for i in d:
    print(i, end="")
    print('\t', end = "")
    print(d[i])

class KYOUTU:
    def __init__(self ,hai):
        self.dk = []
        self.hai = hai
        self.han = 'F'
# b =0 , c = 1by def
    def kyoutuu(self, b, c, max):
        if c < len(self.hai):
            if max < self.hai[b][1]:
                max = self.hai[b][1]
            if int(self.hai[c][0]) >   max:
                if self.han =='F':
                    self.dk.append([self.hai[b][0], max])
                    self.kyoutuu(c, c+1, 0)
                elif self.han =='T':
                    self.dk.append([self.hai[self.sai][0], max])
                    self.han ='F'
                    self.kyoutuu(c, c+1, 0)
            elif  max < int(self.hai[c][1]):
                if c+1 == len(self.hai): ##
                    if self.han =='F':
                        self.dk.append([self.hai[b][0], self.hai[c][1]])
                    elif self.han =='T':
                        self.dk.append([self.hai[self.sai][0],  self.hai[c][1]])
                        self.han ='F'
                else:
                    if  int(self.hai[c][1]) < int(self.hai[c+1][0]) :
                        if self.han =='F':
                            self.dk.append([self.hai[b][0],  self.hai[c][1]])
                            self.kyoutuu(c+1, c+2, 0)
                        elif self.han =='T':
                            self.dk.append([self.hai[self.sai][0],  self.hai[c][1]])
                            self.han ='F'
                            self.kyoutuu(c+1, c+2, 0)
                    else:
                        max = int(self.hai[c][1])
                        self.sai = b
                        self.han = 'T'
                        self.kyoutuu(c, c+1, max)
            else:
                if max < int(self.hai[c][1]):
                    max = int(self.hai[c][1])
                self.kyoutuu(b, c+1, max)
                
        else:
            # if len(self.hai) < b and len(self.hai) < c-1: 
            self.dk.append([self.hai[b][0], self.hai[c-1][1]])

    def jikkoukyoutuu(self):
        self.kyoutuu(0,1,0 )
        dk1 = []
        for i in self.dk:
            dk1.append(tuple(i))
        return dk1


ryou = {}

for i in d:
    con = KYOUTU(d[i]) 
    ryou[i] = con.jikkoukyoutuu()

print('Regions to remove:')
k = {}
for i in ryou:
    reads = open(i)
    e1 = reads.readline()
    # print(e1, "e1")
    e2 = reads.readline()
    while e2 == '\n':
        e2 = reads.readline()
    e3 = e2[::]
    k[i] = sorted(ryou[i], key = lambda kv: int(kv[0]))
    print(i, end='')
    print('\t', end = '')
    print(k[i])
    newl = e2[0:k[i][0][0]]
    for j in range(len(ryou[i])-1):
        newl = newl + e2[k[i][j][1]:k[i][j+1][0]]
    newl = newl + e2[k[i][len(k[i])-1][1]:]
    # newl = []
    # if len(d[i]) == 2:
    #     if k[i][0][1] <= k[i][1][0]:
    #         # print(k[i], i, len(e2), k[i][0][1], k[i][1][0], "aaa")
    #         # newl.append(e2[0:k[0]])
    #         newl.append(e2[0:k[i][0][0]]+e2[k[i][0][1]:k[i][1][0]]+e2[k[i][1][1]:])
    #         # print(e2[k[i][0][1]],e2[k[i][1][0]])
    #         # newl.append(e2[k[3]:])
    #     else:
    #             if k[i][0][1] > k[i][1][1]:
    #                 newl.append(e2[0:k[i][0][0]]+e2[k[i][0][1]:])
    #             else:
    #                 newl.append(e2[0:k[i][0][0]]+e2[k[i][1][1]:])
    #         # newl.append(e2[0:k[0]])
    #         # newl.append(e2[max(k[1], k[3]):)
    # else:
    #     newl.append(e2[0:k[i][0][0]]+ e2[k[i][0][1]:])
    #     # print(k)
    #     # print(k[i])
    #     # if k[i][0][0] > len(e2) -  k[i][0][1]:
    #     #     newl.append(e2[0:k[i][0][0]])
    #     # else:
    #     #     newl.append(e2[k[i][0][1]:])

    f = open(i,  'w')
    f.write(e1)
    for j in newl:
        f.write(j)
    f.close()


    # a = ''
    # filn = i.split('/')[-1]
    # dirn =  i.split('/')[1:-1]
    # for j in dirn:
    #     a  = a+'/'+j
    # print(a+'/pre_trimmed.'+filn)
    # f = open(a+'/pre_trimmed.'+filn, 'w')
    # f.write(e3)
    # for i in newl:
    #     f.write(i)
    # f.close()
