#!/bin/bash
#SBATCH --partition=Orion
#SBATCH --time=47:00:00
#SBATCH --mem=64GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

cd /scratch/nkrell/ReMap_Trimmed_Genes/blast
#merge TAAR and OR data
for file in *_chemo.tblastn
do
        cat "$file" "${file%.*}".blastn > "$file".merged.chemo.blastn
done

#this is changed because the TAARs arent being run
for file in *_chemo.blastn
do
        mv "$file" "$file".merged.chemo.blastn
done

module load bedtools2
module load blast

cd /scratch/nkrell/ReMap_Trimmed_Genes/blast

for file in *.merged.chemo.blastn
do
        python /projects/yohe_lab/genomeGTFtools-master/blast2gff.py -b "$file" -F -l 100 -s 0.2 > "${file%.*}".output.gff3
done

python3 /scratch/nkrell/ReMap_Trimmed_Genes/ReMap_Info_Preserver.py

cd /scratch/nkrell/ReMap_Trimmed_Genes/blast

for file in *.gff3.info
do
        awk -vOFS='\t' '{$3 = $9; print}' "$file" > "$file".name
done

cd /scratch/nkrell/ReMap_Trimmed_Genes/blast

for file in *.output.gff3.info.name
do
        bedtools getfasta -fi /scratch/nkrell/ReMap_Trimmed_Genes/GCF_009914755.1_T2T-CHM13v2.0_genomic.fna -bed /scratch/nkrell/ReMap_Trimmed_Genes/blast/"$file" -s -name -fo /scratch/nkrell/ReMap_Trimmed_Genes/blast/"$file".fa.out
done

#remove exact duplicates
for file in *.out
do
        ~/bbmap/dedupe.sh in="$file" out="${file%.*.*}".fasta ow=t
done

#move to your home directory
cd ~/ora-1.9.1/scripts
for file in /scratch/nkrell/ReMap_Trimmed_Genes/blast/*.name.fasta
do
        perl or.pl -sequence "$file" -a -d --sub "$file".sub.fasta > "$file".ORs.fasta
done

#remove empty first line from fasta file to make up for ORA bug
#this can be run repeatedly without any dataloss
#I added this script to the genomeGTFtools folder for organization
cd /scratch/nkrell/ReMap_Trimmed_Genes/blast
python3 /projects/yohe_lab/genomeGTFtools-master/ORA_Fix.py

#re-remove duplicates
for file in *.fixed.fasta
do
        ~/bbmap/dedupe.sh in="$file" out="${file%.*.*.*}".ORs.clean.fasta ow=t
done