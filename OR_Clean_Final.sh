#!/bin/bash
#SBATCH --partition=Orion
#SBATCH --time=400:00:00
#SBATCH --mem=64GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

#post-processing script for OR_Final.sh data data
cd /scratch/nkrell/Stenella_coeruleoalba/blast
#merge TAAR and OR data
for file in *_chemo.tblastn
do
        cat "$file" "${file%.*}".blastn > "$file".merged.chemo.blastn
done

#this is changed because the TAARs arent being run
for file in *_chemo.tblastn
do
        mv "$file" "$file".merged.chemo.blastn
done

module load bedtools2
module load blast

cd /scratch/nkrell/Stenella_coeruleoalba/blast

for file in *.merged.chemo.blastn
do
        python /projects/yohe_lab/genomeGTFtools-master/blast2gff.py -b "$file" -F -l 100 -s 0.2 > "${file%.*}".output.gff3
done

for file in *.gff3
do
        awk -vOFS='\t' '{$3 = $9; print}' "$file" > "$file".name
done


cd /scratch/nkrell/Stenella_coeruleoalba/blast

for file in *.output.gff3.name
do
        bedtools getfasta -fi /scratch/nkrell/Stenella_coeruleoalba/"${file%_*.*.*.*}".fna -bed /scratch/nkrell/Stenella_coeruleoalba/blast/"$file" -s -name -fo /scratch/nkrell/Stenella_coeruleoalba/blast/"$file".fa.out
done

#remove exact duplicates
for file in *.out
do
        ~/bbmap/dedupe.sh in="$file" out="${file%.*.*}".fasta ow=t
done

#move to your home directory
cd ~/ora-1.9.1/scripts
for file in /scratch/nkrell/Stenella_coeruleoalba/blast/*.name.fasta
do
        perl or.pl -sequence "$file" -a -d --sub "$file".sub.fasta > "$file".ORs.fasta
done

#remove empty first line from fasta file to make up for ORA bug
#this can be run repeatedly without any dataloss
#I added this script to the genomeGTFtools folder for organization
cd /scratch/nkrell/Stenella_coeruleoalba/blast
python3 /projects/yohe_lab/genomeGTFtools-master/ORA_Fix.py

#re-remove duplicates
for file in *.fixed.fasta
do
        ~/bbmap/dedupe.sh in="$file" out="${file%.*.*.*}".ORs.clean.fasta ow=t
done