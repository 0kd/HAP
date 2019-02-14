# arg: counthap

import sys
import os
hikisuu = sys.argv
con_blo = {}
ookisa = {}
contigs_10X=[]

if len(hikisuu)-1 ==0:
	sys.stderr.write("Error: no argument")
else:
	for i in range(len(hikisuu)-1):
		#filename=hikisuu[i+1].split("/")[-1]
		filename=hikisuu[i+1].split("__")[-1]
		filename=filename.split(".")[0]+filename.split(".")[1]
		if not (filename in contigs_10X ):
			contigs_10X.append(filename)
		f1=open(hikisuu[i+1])
		for lineline in f1:
			if lineline != '\n':
				linea=lineline.split()
				if linea[0]=="rname":
					pass
				else:
					if linea[2] == linea[3]:
						pass
					elif int(linea[2]) > int(linea[3]):
						if linea[1] in con_blo:
							con_blo[linea[1]][filename+"left"]=linea[2]+":"+linea[3]#+"@"+linea[2]+">"+linea[3])
						else:
							#con_blo[linea[1]]=[filename+"_left"+" :"+linea[2]+">"+linea[3]]
							con_blo[linea[1]]={}
							con_blo[linea[1]][filename+"left"]=linea[2]+":"+linea[3]#+"@"+linea[2]+">"+linea[3])
					elif int(linea[3]) > int(linea[2]):
						if linea[1] in con_blo:
							con_blo[linea[1]][filename+"right"]=linea[2]+":"+linea[3]#+"@"+linea[2]+">"+linea[3])
						else:
							#con_blo[linea[1]]=[filename+"_right"+" :"+linea[3]+">"+linea[2]]
							con_blo[linea[1]]={}
							con_blo[linea[1]][filename+"right"]=linea[2]+":"+linea[3]#+"@"+linea[2]+">"+linea[3])
					else:
						sys.stderr.write("There may be strange row")


keyd = list(con_blo.keys())
valued=[]
for j in keyd:
	valued.append([])
	for l in con_blo[j].keys():
		valued[-1].append(l)
# 		
# valued2 = con_blo.values()
# print(valued2)
# valued=[]
# for i in  range(len(valued2)):
# 	valued.append(valued2[i].keys())
dotn={}
KOUNT=0
for i in contigs_10X:
	KOUNT+=1
for k in range(len(con_blo)):
	for l in range(len(valued[k])):
		for m in range(l+1, len(valued[k])):
			if keyd[k] in dotn:
				dotn[keyd[k]].append({valued[k][l],valued[k][m]})
			else:
				dotn[keyd[k]]=[]
				dotn[keyd[k]].append({valued[k][l],valued[k][m]})

valval=[]
for a in range(len(dotn.values())):
	for b in list(dotn.values())[a]:
		if b not in valval:
			valval.append(b)
namae=contigs_10X[0].split("X")[0]+"X"
if namae+"counthap" not in os.listdir("."):
	with open(namae+"counthap", "w") as f:
		for k in valval:
			st="#qname"
			for ij in list(k):
				st=st+" "+ij
			f.write(st)
			f.write('\n')
			f.write('\n')
			for iii in dotn:
				for h in range(len(dotn[iii])):
					#print(k,  dotn[iii][h],  "asd")
					if dotn[iii][h]== k:
						f.write(iii+" "+con_blo[iii][list(k)[0]]+" "+con_blo[iii][list(k)[1]])
						f.write('\n')
			f.write('\n')				
			f.write("#end")
			f.write('\n')				
					#x10apb[dotn[i][j]]=i			
else:
	sys.stderr.write(namae+"counthap already exists.")
contigs_10X_num=[]
contigs_10X_0=[]
for i in range(len(contigs_10X)):
	num=contigs_10X[i].split("X")[1]
	num0=contigs_10X[i].split("X")[0]
	contigs_10X_num.append(num)
	contigs_10X_0.append(num0+"X")

contigs_10X_num.sort()

contigs_10X_n1=[]
for i in range(len(contigs_10X)):
	contigs_10X_n1.append(contigs_10X_0[0]+contigs_10X_num[i])
#print(contigs_10X_n)

cand1=[]
group1=[]
group2=[]
with open(namae+"counthap") as f:
	for lineline in f:
		if lineline != '\n':
			linea=lineline.split()
			if linea[0]=="#qname":
				cand1.append([linea[1], linea[2]])
				hikizan1=0
				hikizan2=0
			elif  linea[0]=="#end":
				cand1[-1].append(hikizan1)
				cand1[-1].append(hikizan2)
			else:
				hikizan1=abs(int(linea[1].split(":")[0])-int(linea[1].split(":")[1]))+hikizan1
				hikizan2=abs(int(linea[2].split(":")[0])-int(linea[2].split(":")[1]))+hikizan2

print(cand1)
			
def group5(contigs_10X_n,cand):
#print(cand,"cand")
	group1=[]
	group2=[]
	group1.append(contigs_10X_n[0]+"left")
	group2.append(contigs_10X_n[0]+"right")
	joutai=[]
	for i in  range(len(contigs_10X_n)-1):
		kouho1=[0,0,0]
		kouho2=[0,0,0]
		kouho3=[0,0,0]
		kouho4=[0,0,0]
		for j in range(len(cand)):
			if contigs_10X_n[i]+"left" in cand[j]:
				if contigs_10X_n[i+1]+"left" in cand[j]:
					kouho1=[contigs_10X_n[i+1]+"left",cand[j][2], cand[j][3]]
	#				if contigs_10X_n[i]+"left" in group1:
	#					group1.append(contigs_10X_n[i+1]+"left")
	#				if contigs_10X_n[i]+"left" in group2:
	#					group2.append(contigs_10X_n[i+1]+"left")
				if contigs_10X_n[i+1]+"right" in cand[j]:
					kouho2=[contigs_10X_n[i+1]+"right",cand[j][2], cand[j][3]]
	#				if contigs_10X_n[i]+"left" in group1:
	#					group1.append(contigs_10X_n[i+1]+"right")
	#				if contigs_10X_n[i]+"left" in group2:
	#					group2.append(contigs_10X_n[i+1]+"right")
			if contigs_10X_n[i]+"right" in cand[j]:
				if contigs_10X_n[i+1]+"left" in cand[j]:
					kouho3=[contigs_10X_n[i+1]+"left", cand[j][2], cand[j][3]]
	#				if contigs_10X_n[i]+"right" in group1:
	#					group1.append(contigs_10X_n[i+1]+"left")
	#				if contigs_10X_n[i]+"right" in group2:
	#					group2.append(contigs_10X_n[i+1]+"left")
				if contigs_10X_n[i+1]+"right" in cand[j]:
					kouho4=[contigs_10X_n[i+1]+"right",cand[j][2], cand[j][3]]
	#				if contigs_10X_n[i]+"right" in group1:
	#					group1.append(contigs_10X_n[i+1]+"right")
	#				if contigs_10X_n[i]+"right" in group2:
	#					group2.append(contigs_10X_n[i+1]+"right")
	#	if (kouho1 != [0,0,0] and kouho2 != [0,0,0] and kouho3 !=[0,0,0] and kouho4 != [0,0,0]) or (kouho1 != [0,0,0] and kouho2 != [0,0,0] and kouho3 ==[0,0,0] and kouho4 != [0,0,0]) or (kouho1 != [0,0,0] and kouho2 == [0,0,0] and kouho3 != [0,0,0] and kouho4 != [0,0,0]) or(kouho1 != [0,0,0] and kouho2 != [0,0,0] and kouho3 !=[0,0,0] and kouho4 == [0,0,0]) or (kouho1 == [0,0,0] and kouho2 != [0,0,0] and kouho3 !=[0,0,0] and kouho4 != [0,0,0]):
		cis=int(kouho1[1])*int(kouho1[2])+int(kouho4[1])*int(kouho4[2])
		trans=int(kouho2[1])*int(kouho2[2])+int(kouho3[1])*int(kouho3[2])
		if cis > trans:
			if contigs_10X_n[i]+"right" in group1:
				group1.append(contigs_10X_n[i+1]+"right")
			if contigs_10X_n[i]+"right" in group2:
				group2.append(contigs_10X_n[i+1]+"right")
			if contigs_10X_n[i]+"left" in group1:
				group1.append(contigs_10X_n[i+1]+"left")
			if contigs_10X_n[i]+"left" in group2:
				group2.append(contigs_10X_n[i+1]+"left")
		elif cis < trans:
			if contigs_10X_n[i]+"right" in group1:
				group1.append(contigs_10X_n[i+1]+"left")
			if contigs_10X_n[i]+"right" in group2:
				group2.append(contigs_10X_n[i+1]+"left")
			if contigs_10X_n[i]+"left" in group1:
				group1.append(contigs_10X_n[i+1]+"right")
			if contigs_10X_n[i]+"left" in group2:
				group2.append(contigs_10X_n[i+1]+"right")
		joutai.append([contigs_10X_n[i]])
		for ki in range(len([kouho1, kouho2 , kouho3, kouho4])):
			if [kouho1, kouho2 , kouho3, kouho4][ki] !=[0,0,0]:
				if ki ==0:
					joutai[-1].append("R-R")
				if ki ==1:
					joutai[-1].append("R-L")
				if ki ==2:
					joutai[-1].append("L-R")
				if ki ==3:
					joutai[-1].append("L-L")
	
		joutai[-1].append(cis)
		joutai[-1].append(trans)
	joutai.append([contigs_10X_n[len(contigs_10X_n)-1]])
	return group1, group2, joutai
			
		

contigs_10X_n2=[]
contigs_10X_n3=[]
contigs_10X_n4=[]
contigs_10X_n5=[]
contigs_10X_n6=[]
for i in range(len(contigs_10X_n1)):
	if i%2 == 0:
		contigs_10X_n2.append(contigs_10X_n1[i])		
	else:
	        contigs_10X_n3.append(contigs_10X_n1[i])

for i in range(len(contigs_10X_n1)):
	if i%3 == 0:
		contigs_10X_n4.append(contigs_10X_n1[i])		
	elif i%3 == 1:
	        contigs_10X_n5.append(contigs_10X_n1[i])
	elif i%3 == 2:
	        contigs_10X_n6.append(contigs_10X_n1[i])
	
sa1=group5(contigs_10X_n1,cand1)
sa2=group5(contigs_10X_n2,cand1)
sa3=group5(contigs_10X_n3,cand1)
sa4=group5(contigs_10X_n4,cand1)
sa5=group5(contigs_10X_n5,cand1)
sa6=group5(contigs_10X_n6,cand1)

print(sa1)
ko1=[[]]
ko2=[[]]
ko3=[[]]
kount=0
for i in range(len(sa1[0])-1):
	if (sa1[2][i][-1] == 0 and sa1[2][i][-2] != 0) or (sa1[2][i][-2] == 0 and sa1[2][i][-1] != 0):
		ko1[-1].append(sa1[0][i])		
		ko2[-1].append(sa1[1][i])
		ko3[-1].append(sa1[2][i])
	else:
		ko1.append([])
		ko2.append([])
		ko3.append([])
nagasa=0
nagasa1=0
for i in ko1:
	nagasa=len(i)
	if nagasa > nagasa1:
		nagasa1=nagasa
		ko1f=i
nagasa=0
nagasa1=0
for i in ko2:
	nagasa=len(i)
	if nagasa > nagasa1:
		nagasa1=nagasa
		ko2f=i
nagasa=0
nagasa1=0
for i in ko3:
	nagasa=len(i)
	if nagasa > nagasa1:
		nagasa1=nagasa
		ko3f=i
print(ko3f)
fincon=[]

for i in ko3f:
	con1=i[0].split("X")[0]
	con2=i[0].split("X")[1]
	fincon.append(con1+"X"+"."+con2)
print(fincon,"fincon")
namae2=namae.split("_")[0]
filess=os.listdir("/grid/yoshimura/human/"+namae2+"/haplotype/counthap/")

group1ko=[]
group2ko=[]

for j in fincon:
	s= j.split(".")[0]+j.split(".")[1]
	if s+"right" in ko1f:
		for i in filess:
			if j in i:
				f1=open("/grid/yoshimura/human/"+namae2+"/haplotype/counthap/"+i)
				for lineline in f1:
					if lineline != '\n':
						linea=lineline.split()
						if linea[0]=="rname":
							pass
						else:
							if linea[2] == linea[3]:
								pass
							elif int(linea[2]) > int(linea[3]):
								if linea[1] not in group1ko:
									group1ko.append(linea[1])
							elif int(linea[3]) > int(linea[2]):
								if linea[1] not in group2ko:
									group2ko.append(linea[1])
							else:
								sys.stderr.write("There may be strange row")
				f1.close()
	if s+"right" in ko2f:
		for i in filess:
			if j in i:
				f1=open("/grid/yoshimura/human/"+namae2+"/haplotype/counthap/"+i)
				for lineline in f1:
					if lineline != '\n':
						linea=lineline.split()
						if linea[0]=="rname":
							pass
						else:
							if linea[2] == linea[3]:
								pass
							elif int(linea[2]) > int(linea[3]):
								if linea[1] not in group2ko:
									group2ko.append(linea[1])
							elif int(linea[3]) > int(linea[2]):
								if linea[1] not in group1ko:
									group1ko.append(linea[1])
							else:
								sys.stderr.write("There may be strange row")
				f1.close()
print(group1ko)
print(group2ko)
				
ff=open("/grid/yoshimura/human/"+namae2+"/haplotype/"+namae2+".HLA_contig.sam")

if namae+"_1.fasta" not in os.listdir("."):
	with open(namae+"_1.fasta", "w") as f:
		for linel in ff:
			for j in group1ko:
				linea=linel.split()
				if linea[0]==j:
					f.write(">"+linea[0])
					f.write('\n')
					f.write(linea[9])
					f.write('\n')
else:
	sys.stderr.write(namae+"_1.fasta already exists."+'\n')
ff.close()

ff=open("/grid/yoshimura/human/"+namae2+"/haplotype/"+namae2+".HLA_contig.sam")
if namae+"_2.fasta" not in os.listdir("."):
	with open(namae+"_2.fasta", "w") as f:
		for linel in ff:
			for j in group2ko:
				linea=linel.split()
				if linea[0]==j:
					f.write(">"+linea[0])
					f.write('\n')
					f.write(linea[9])
					f.write('\n')
else:
	sys.stderr.write(namae+"_2.fasta already exists."+'\n')
ff.close()

# 
# kofin=ko3f-fincon
# for j in kofin:
# 
