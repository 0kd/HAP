#  args: sam, counthap

import pathlib as pl
import sys
import crit


valuea = 0.0001  # minimum error rate to dismiss
samtofasta = []

for i in sys.argv:
    if i.split()[-1] == 'sam':
        filen = pl.Path(i).read_text().split('\n')
        for j in filen:
            rows = j.split('\t')
            if int(rows[1]) < 17:
                samtofasta.append({rows[0], rows[9]})

for i in sys.argv:
    if i.split()[-1] == 'counthap':
        filen = pl.Path(i).read_text().split('\n')
        fastar = pl.Path(i+'.right.fasta')
        fastarl = []
        fastal = pl.Path(i+'.left.fasta')
        fastall = []

        for j in filen:
            rown = j.split('\t')

            if len(j) == 0:
                pass
            elif j[0] == 'rname':
                pass
            else:
                rname = j[0]
                evalue = crit.keisan(j[2], j[3], j[4])

                if evalue < valuea:
                    if int(j[2]) < int(j[3]):
                        sequen = samtofasta.get(rname)
                        fastarl.append(rname+'\n')
                        fastarl.append(sequen+'\n')
                    elif int(j[2]) > int(j[3]):
                        sequen = samtofasta.get(rname)
                        fastall.append(rname+'\n')
                        fastall.append(sequen+'\n')

        for k in fastarl:
            fastar.write_text(rname+'\n')
            fastar.write_text(sequen+'\n')
        for k in fastall:
            fastal.write_text(rname+'\n')
            fastal.write_text(sequen+'\n')
