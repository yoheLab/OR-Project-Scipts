#!/bin/bash
#SBATCH --partition=Nebula
#SBATCH --time=47:00:00
#SBATCH --mem=124GB
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=8
#SBATCH --array=1-1

module load blast

file=$(sed -n -e "${SLURM_ARRAY_TASK_ID}p" /scratch/nkrell/Stenella_coeruleoalba/files.txt)

cd /scratch/nkrell/Stenella_coeruleoalba/

makeblastdb  -in /scratch/nkrell/Stenella_coeruleoalba/"$file" -title "${file%.*}" -dbtype nucl -out /scratch/nkrell/Stenella_coeruleoalba/blastdb/"${file%.*}"
blastn -query /scratch/nkrell/Stenella_coeruleoalba/blast_reptileChemo_TAAR.fasta -db /scratch/nkrell/Stenella_coeruleoalba/blastdb/"${file%.*}" -num_threads 8 -num_alignments 1000 -outfmt 6 -out /scratch/nkrell/Stenella_coeruleoalba/blast/"${file%.*}"_chemo.blastn
makeblastdb  -in /scratch/nkrell/Stenella_coeruleoalba/"$file" -title "${file%.*}" -dbtype nucl -out /scratch/nkrell/Stenella_coeruleoalba/blastdb/"${file%.*}"
tblastn -query /scratch/nkrell/Stenella_coeruleoalba/blast_reptileChemo.fasta -db /scratch/nkrell/Stenella_coeruleoalba/blastdb/"${file%.*}" -num_threads 8 -num_alignments 1000 -outfmt 6 -out /scratch/nkrell/Stenella_coeruleoalba/blast/"${file%.*}"_chemo.tblastn
