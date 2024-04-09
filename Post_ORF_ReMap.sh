#!/bin/bash
#SBATCH --partition=Orion
#SBATCH --time=47:00:00
#SBATCH --mem=124GB
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=4
#SBATCH --array=1-1

module load blast

file=$(sed -n -e "${SLURM_ARRAY_TASK_ID}p" /scratch/nkrell/ReMap_Trimmed_Genes/files.txt)

cd /scratch/nkrell/ReMap_Trimmed_Genes/

#make one database, since I'm running several things againsta single genome
makeblastdb  -in /scratch/nkrell/ReMap_Trimmed_Genes/"$file" -title "${file%.*}" -dbtype nucl -out /scratch/nkrell/ReMap_Trimmed_Genes/blastdb/"${file%.*}"
echo "blastdb done"

#g2or Iter Coding
blastn -query /scratch/nkrell/ReMap_Trimmed_Genes/T2T_g2or_Iter_Coding.korff.fasta.trimmed.picked.fasta -db /scratch/nkrell/ReMap_Trimmed_Genes/blastdb/"${file%.*}" -num_threads 4 -num_alignments 1000 -perc_identity 100 -outfmt 6 -out /scratch/nkrell/ReMap_Trimmed_Genes/blast/T2T_g2or_Iter_Coding_chemo.blastn
echo "g2or Iter Coding done"

#g2or Anno Coding
blastn -query /scratch/nkrell/ReMap_Trimmed_Genes/T2T_g2or_Anno_Coding.korff.fasta.trimmed.picked.fasta -db /scratch/nkrell/ReMap_Trimmed_Genes/blastdb/"${file%.*}" -num_threads 4 -num_alignments 1000 -perc_identity 100 -outfmt 6 -out /scratch/nkrell/ReMap_Trimmed_Genes/blast/T2T_g2or_Anno_Coding_chemo.blastn
echo "g2or Anno Coding done"

#ORA Coding
blastn -query /scratch/nkrell/ReMap_Trimmed_Genes/T2T_ORA_ORs_Only_Coding.korff.fasta.trimmed.picked.fasta -db /scratch/nkrell/ReMap_Trimmed_Genes/blastdb/"${file%.*}" -num_threads 4 -num_alignments 1000 -perc_identity 100 -outfmt 6 -out /scratch/nkrell/ReMap_Trimmed_Genes/blast/T2T_ORA_Coding_chemo.blastn
echo "ORA Coding done"

#g2or Iter Pseudo
blastn -query /scratch/nkrell/ReMap_Trimmed_Genes/T2T_g2or_Iter_Pseudo.korff.fasta -db /scratch/nkrell/ReMap_Trimmed_Genes/blastdb/"${file%.*}" -num_threads 4 -num_alignments 1000 -perc_identity 100 -outfmt 6 -out /scratch/nkrell/ReMap_Trimmed_Genes/blast/T2T_g2or_Iter_Pseudo_chemo.blastn
echo "g2or Iter Pseudo done"

#g2or Anno Pseudo
blastn -query /scratch/nkrell/ReMap_Trimmed_Genes/T2T_g2or_Anno_Pseudo.korff.fasta -db /scratch/nkrell/ReMap_Trimmed_Genes/blastdb/"${file%.*}" -num_threads 4 -num_alignments 1000 -perc_identity 100 -outfmt 6 -out /scratch/nkrell/ReMap_Trimmed_Genes/blast/T2T_g2or_Anno_Pseudo_chemo.blastn
echo "g2or Anno Pseudo done"
