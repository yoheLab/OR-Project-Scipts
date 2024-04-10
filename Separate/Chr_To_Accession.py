import os
import sys
import time


newFile = open("T2T_JHU_Anno_Accession.gff3", "w")

accList = [("NC_060925.1", "chr1"),
		   ("NC_060926.1", "chr2"),
		   ("NC_060927.1", "chr3"),
		   ("NC_060928.1", "chr4"),
		   ("NC_060929.1", "chr5"),
		   ("NC_060930.1", "chr6"),
		   ("NC_060931.1", "chr7"),
		   ("NC_060932.1", "chr8"),
		   ("NC_060933.1", "chr9"),
		   ("NC_060934.1", "chr10"),
		   ("NC_060935.1", "chr11"),
		   ("NC_060936.1", "chr12"),
		   ("NC_060937.1", "chr13"),
		   ("NC_060938.1", "chr14"),
		   ("NC_060939.1", "chr15"),
		   ("NC_060940.1", "chr16"),
		   ("NC_060941.1", "chr17"),
		   ("NC_060942.1", "chr18"),
		   ("NC_060943.1", "chr19"),
		   ("NC_060944.1", "chr20"),
		   ("NC_060945.1", "chr21"),
		   ("NC_060946.1", "chr22"),
		   ("NC_060947.1", "chrX"),
		   ("NC_060948.1", "chrY")]


with open("T2T_JHU_Anno.gff3") as fh:
	for line in fh:
		if line.startswith("#"):
			continue
		else:
			line = line.split('\t')
			chromosome = line[0]
			for pair in accList:
				if chromosome == pair[1]:
					chromosome = pair[0]
			line.pop(0)
			newLine = "\t".join(line)
			newLine = chromosome + "\t" + newLine
			#print(newLine)
			newFile.write(newLine)









newFile.close()







#chr1	Liftoff	gene	6047	13941	.	-	.	ID=LOC124900618;gene_name=LOC124900618;db_xref=GeneID:124900618;gbkey=Gene;gene=LOC124900618;gene_biotype=lncRNA;coverage=1.0;sequence_ID=0.965;extra_copy_number=0;copy_num_ID=LOC124900618_0










