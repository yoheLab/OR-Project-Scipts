import os

for file in os.listdir():
	if file.endswith("_Final.korff"):
		with open(file) as fh:
			newFile = open(file + ".gff3", "w")
			for line in fh:
				if line.startswith("Identifier"):
					continue

				line = line.strip('\n')
				line = line.split('\t')

				#Chromosome  Source  Type  Start  End  Score  Sense  Phase  Attribute
				tab = '\t'
				newFile.write(line[2] + tab + line[1] + tab + "Gene" + tab + line[3] + tab + line[4] + tab + "." + tab + line[5] + tab + "." + tab + line[9])
				newFile.write('\n')
			newFile.close()