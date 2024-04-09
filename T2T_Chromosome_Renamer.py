newFile = open("T2T_Chromosomes_Fixed.fasta", "w")
with open("GCF_009914755.1_T2T-CHM13v2.0_genomic.fasta") as fh:
	for line in fh:

		line = line.strip("\n")

		if line == ">NC_060925.1 Homo sapiens isolate CHM13 chromosome 1, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr1")
			newFile.write("\n")

		elif line == ">NC_060926.1 Homo sapiens isolate CHM13 chromosome 2, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr2")
			newFile.write("\n")

		elif line == ">NC_060927.1 Homo sapiens isolate CHM13 chromosome 3, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr3")
			newFile.write("\n")

		elif line == ">NC_060928.1 Homo sapiens isolate CHM13 chromosome 4, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr4")
			newFile.write("\n")

		elif line == ">NC_060929.1 Homo sapiens isolate CHM13 chromosome 5, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr5")
			newFile.write("\n")

		elif line == ">NC_060930.1 Homo sapiens isolate CHM13 chromosome 6, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr6")
			newFile.write("\n")

		elif line == ">NC_060931.1 Homo sapiens isolate CHM13 chromosome 7, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr7")
			newFile.write("\n")

		elif line == ">NC_060932.1 Homo sapiens isolate CHM13 chromosome 8, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr8")
			newFile.write("\n")

		elif line == ">NC_060933.1 Homo sapiens isolate CHM13 chromosome 9, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr9")
			newFile.write("\n")

		elif line == ">NC_060934.1 Homo sapiens isolate CHM13 chromosome 10, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr10")
			newFile.write("\n")

		elif line == ">NC_060935.1 Homo sapiens isolate CHM13 chromosome 11, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr11")
			newFile.write("\n")

		elif line == ">NC_060936.1 Homo sapiens isolate CHM13 chromosome 12, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr12")
			newFile.write("\n")

		elif line == ">NC_060937.1 Homo sapiens isolate CHM13 chromosome 13, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr13")
			newFile.write("\n")

		elif line == ">NC_060938.1 Homo sapiens isolate CHM13 chromosome 14, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr14")
			newFile.write("\n")

		elif line == ">NC_060939.1 Homo sapiens isolate CHM13 chromosome 15, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr15")
			newFile.write("\n")

		elif line == ">NC_060940.1 Homo sapiens isolate CHM13 chromosome 16, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr16")
			newFile.write("\n")

		elif line == ">NC_060941.1 Homo sapiens isolate CHM13 chromosome 17, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr17")
			newFile.write("\n")

		elif line == ">NC_060942.1 Homo sapiens isolate CHM13 chromosome 18, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr18")
			newFile.write("\n")

		elif line == ">NC_060943.1 Homo sapiens isolate CHM13 chromosome 19, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr19")
			newFile.write("\n")

		elif line == ">NC_060944.1 Homo sapiens isolate CHM13 chromosome 20, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr20")
			newFile.write("\n")

		elif line == ">NC_060945.1 Homo sapiens isolate CHM13 chromosome 21, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr21")
			newFile.write("\n")

		elif line == ">NC_060946.1 Homo sapiens isolate CHM13 chromosome 22, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chr22")
			newFile.write("\n")

		elif line == ">NC_060947.1 Homo sapiens isolate CHM13 chromosome X, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chrX")
			newFile.write("\n")

		elif line == ">NC_060948.1 Homo sapiens isolate NA24385 chromosome Y, alternate assembly T2T-CHM13v2.0":
			newFile.write(">chrY")
			newFile.write("\n")

		else:
			newFile.write(line)
			newFile.write("\n")

newFile.close()




