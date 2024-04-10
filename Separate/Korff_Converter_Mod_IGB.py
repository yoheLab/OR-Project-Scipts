import os

for file in os.listdir():
	if file.endswith(".korff"):
		with open(file) as fh:
			newFile = open(file + ".gff3", "w")
			for line in fh:
				if line.startswith("Identifier"):
					continue

				line = line.strip('\n')
				line = line.split('\t')
				attribute = "gene=" + line[0] + ";"
				attribute += "class=" + line[6] + ";"
				attribute += "coding_status="  + line[7] + ";"
				#Chromosome  Source  Type  Start  End  Score  Sense  Phase  Attribute
				tab = '\t'
				#newFile.write(line[2] + tab + line[1] + tab + "Gene" + tab + line[3] + tab + line[4] + tab + "." + tab + line[5] + tab + "." + tab + line[9])
				newFile.write(line[2] + tab + line[1] + tab + "Gene" + tab + line[3] + tab + line[4] + tab + "." + tab + line[5] + tab + "." + tab + attribute)
				newFile.write('\n')
			newFile.close()