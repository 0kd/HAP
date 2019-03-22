import groups0313 as g3
import os

direc1 = []
group1 = g3.group1
group2 = g3.group2

for i in group1:
    dire = i.split('counthap')[1]
    numb = i.split('.')[1]
    direc1.append('/work/kudo/HAP/B022_hap_2/'+numb+'_haplo/'+numb+'.counthap.'+dire+'.fasta')


os.system('rm test11')
os.system('touch test11')




direc2 = []
for i in group2:
    dire = i.split('counthap')[1]
    numb = i.split('.')[1]
    direc2.append('/work/kudo/HAP/B022_hap_2/'+numb+'_haplo/'+numb+'.counthap.'+dire+'.fasta')

os.system('rm test22')
os.system('touch test22')


for i in direc1:
    os.system("cat "+i+" >> test11")
for i in direc2:
    os.system("cat "+i+" >> test22")





