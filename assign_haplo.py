import groups0313 as g3
import os

direc1 = []
group1 = g3.group1
group2 = g3.group2

for i in group1:
    dire = i.split('counthap')[1]
    numb = i.split('.')[1]
    direc1.append('/work/kudo/HAP/B022_hap_2/'+numb+'_haplo/'+numb+'.counthap.'+dire+'.fasta')


os.system('rm test1')
os.system('touch test1')

for i in direc1:
    os.system("cat "+i+" >> test1")



direc2 = []
for i in group2:
    dire = i.split('counthap')[1]
    numb = i.split('.')[1]
    direc2.append('/work/kudo/HAP/B022_hap_2/'+numb+'_haplo/'+numb+'.counthap.'+dire+'.fasta')

os.system('rm test2')
os.system('touch test2')

for i in direc2:
    os.system("cat "+i+" >> test2")

