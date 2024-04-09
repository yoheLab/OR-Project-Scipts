#!/bin/bash
#SBATCH --partition=Nebula
#SBATCH --time=47:00:00
#SBATCH --mem=64GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

cd /scratch/nkrell/Classify

cd ~/ora-1.9.1/scripts
for file in /scratch/nkrell/Classify/*_Merged.fasta
do
        perl or.pl -sequence "$file" -a -d --sub "$file".sub.fasta > "$file".ORs.fasta
done

cd /scratch/nkrell/Classify
python3 /projects/yohe_lab/genomeGTFtools-master/ORA_Fix.py



