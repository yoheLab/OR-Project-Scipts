#!/bin/bash
#SBATCH --partition=Orion
#SBATCH --time=47:00:00
#SBATCH --mem=6GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --array=1-23

file=$(sed -n -e "${SLURM_ARRAY_TASK_ID}p" /scratch/nkrell/BFA/files.txt)

python3 PBFA.py T2T_ORA_ORs_Only_Coding.korff.fasta.trimmed.picked "${file}"
