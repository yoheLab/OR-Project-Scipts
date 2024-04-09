#!/bin/bash
#SBATCH --partition=Nebula
#SBATCH --time=47:00:00
#SBATCH --mem=64GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

cd /scratch/nkrell/JHU_Anno

module load bedtools2

python3 /scratch/nkrell/JHU_Anno/PipeLine_Info_Preserver.py

cd /scratch/nkrell/JHU_Anno

for file in *.gff3.info
do
        awk -vOFS='\t' '{$3 = $9; print}' "$file" > "$file".name
done

bedtools getfasta -fi GCF_009914755.1_T2T-CHM13v2.0_genomic.fasta -bed T2T_JHU_Anno.gff3 -s -name -fo JHU_Anno.fasta

