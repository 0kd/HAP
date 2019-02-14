filennn=B022_filname.txt
numnum=2
ls  /grid/yoshimura/human/B022/haplotype/counthap/*.HLA.hap__B022_10X.*.counthap  | awk -F'.' '{print $(NF-1)}'  | sort -n | uniq > $filennn
ls -l /grid/yoshimura/human/B022/haplotype/B022.HLA_contig.fasta | awk '{ print $5 }' >> $filennn
python /work/kudo/HAP/syuukeifilename.py $filennn >  $filennn"_syuukei"
for k in $( ls  /grid/yoshimura/human/B022/haplotype/counthap/*.HLA.hap__B022_10X.*.counthap  | awk -F'.' '{print $(NF-1)}'  | sort -n | uniq)
do
gsize=$(sed -n ${numnum}P $filennn"_syuukei")
numnum=$((numnum+1))
for i in /grid/yoshimura/human/B022/haplotype/counthap/*.HLA.hap__B022_10X.${k}.counthap
do
namae=$(echo $i | awk -F'.' '{print $(NF-1)}'  )
if [ -e '/work/kudo/HAP/B022_hap' ]; then
echo ''
else
mkdir 'B022_hap'
fi
if [ -e '/work/kudo/HAP/B022_hap/'$namae'_haplo' ]; then
echo ''
else
mkdir /work/kudo/HAP/B022_hap/$namae'_haplo' 
cd /work/kudo/HAP/B022_hap/$namae'_haplo'/ 
cp  /grid/yoshimura/human/B022/haplotype/haplo_fasta/mk_haplo_fasta.pl  /work/kudo/HAP/B022_hap/$namae'_haplo'/mk_haplo_fasta.pl
###
sed -e 's/genomeSize=2.3m/genomeSize='$gsize'/g' /grid/yoshimura/human/B022/haplotype/haplo_fasta/canu.sh > /work/kudo/HAP/B022_hap/$namae'_haplo'/canu.sh
if [ -e '/work/kudo/HAP/B022_hap/'$namae'.counthap' ]; then
echo ''
else
echo $namae":"
for k in  /grid/yoshimura/human/B022/haplotype/counthap/*.HLA.hap__B022_10X.${namae}.counthap
do
echo $(ls -lh $k)
done
cat /grid/yoshimura/human/B022/haplotype/counthap/*.HLA.hap__B022_10X.${namae}.counthap  | awk '/./{print $0}'> $namae.counthap
perl mk_haplo_fasta.pl $namae.counthap /grid/yoshimura/human/B022/haplotype/alignment/*
bash /work/kudo/HAP/B022_hap/$namae'_haplo'/canu.sh $namae.counthap.left.fasta
bash /work/kudo/HAP/B022_hap/$namae'_haplo'/canu.sh $namae.counthap.right.fasta
fi
fi
cd /work/kudo/HAP/
done
done
