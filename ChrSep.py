import os

data = list()

with open("GCF_009914755.1_T2T-CHM13v2.0_genomic.fna") as fh:
	for line in fh:
		line = line.strip("\n")
		if line.startswith(">"):
			if tempSeq == "":
				tempHeader = line
			elif tempSeq != "":
				data.append(tuple([tempHeader, tempSeq]))
				tempHeader = line
				tempSeq = ""
		else:
			tempSeq += line
data.append(tuple([tempHeader, tempSeq]))
tempHeader = ""
tempSeq = ""

for entry in data:
	fileName = entry[0].split(" ")
	fileName = fileName[6]
	fileName = "Chr_" + fileName
	fileName += "_T2T_Genome.fna"

	newFile = opne(fileName, "w")
	newFile.write(entry[0])
	newFile.write('\n')
	newFile.write(entry[1])
	newFile.write('\n')
	newFile.close()