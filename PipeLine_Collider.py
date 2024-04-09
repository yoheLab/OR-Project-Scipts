
g2orList = list()
ORAList = list()

ORA_New = list()
g2or_New = list()

ORA_Seqs = list()
g2or_Seqs = list()

newFile = open("Near_Matching_Cords.korff", "w")
newFile2 = open("Matching_Sequences.korff", "w")
newFile3 = open("ORA_Excess.korff", "w")
newFile4 = open("g2or_Excess.korff", "w")
tab = '\t'
newFile.write("Identifier" + tab + "Source" + tab + "Chromosome" + tab + "Start" + tab + "End" + tab + "Sense" + tab + "Class" + tab + "CodingStatus" + tab + "Sequence" + tab + "Attribute" + '\n')
newFile2.write("Identifier" + tab + "Source" + tab + "Chromosome" + tab + "Start" + tab + "End" + tab + "Sense" + tab + "Class" + tab + "CodingStatus" + tab + "Sequence" + tab + "Attribute" + '\n')
newFile3.write("Identifier" + tab + "Source" + tab + "Chromosome" + tab + "Start" + tab + "End" + tab + "Sense" + tab + "Class" + tab + "CodingStatus" + tab + "Sequence" + tab + "Attribute" + '\n')
newFile4.write("Identifier" + tab + "Source" + tab + "Chromosome" + tab + "Start" + tab + "End" + tab + "Sense" + tab + "Class" + tab + "CodingStatus" + tab + "Sequence" + tab + "Attribute" + '\n')



with open("T2T_g2or_Iter.korff") as fh:
	for line in fh:
		if line.startswith("Identifier"):
			continue
		line = line.strip('\n')
		line = line.split('\t')
		g2orList.append(line)
print("Read in: " + str(len(g2orList)))
with open("T2T_ORA.korff") as fh:
	for line in fh:
		if line.startswith("Identifier"):
			continue
		line = line.strip('\n')
		line = line.split('\t')
		ORAList.append(line)
print("Read in: " + str(len(ORAList)))

#for gene in g2orList:
	#print(gene)
#for gene in ORAList:
	#print(gene)
for gene1 in ORAList:
	for gene2 in g2orList:

		if gene1[2] != gene2[2]:

			start1 = int(gene1[3])
			end1 = int(gene1[4])
			start2 = int(gene2[3])
			end2 = int(gene2[4])

			start_dist = abs(start1 - start2)
			end_dist = abs(end1 - end2)

			alt_start_dist = abs(start1 - end2)
			alt_end_dist = abs(end1 - start2)

			if ((start_dist <= 150) and (end_dist <= 150)) or ((alt_start_dist <= 150) and (alt_end_dist <= 150)):
				newFile.write("\t".join(gene1))
				newFile.write('\n')

		




for gene1 in ORAList:
	for gene2 in g2orList:
		if gene1[8].upper() == gene2[8].upper():
			newFile2.write("\t".join(gene1))
			newFile2.write('\n')



ORA_New = ORAList
g2or_New = g2orList

print(str(len(ORA_New)))
print(str(len(g2or_New)))

for gene in g2orList:
	g2or_Seqs.append(gene[8])

for gene in ORAList:
	ORA_Seqs.append(gene[8])

for gene in ORA_New:
	if gene[8] in g2or_Seqs:
		ORA_New.remove(gene)

for gene in g2or_New:
	if gene[8] in ORA_Seqs:
		g2or_New.remove(gene)   

print(str(len(ORA_New)))
print(str(len(g2or_New)))

for gene in ORA_New:
	newFile3.write("\t".join(gene))
	newFile3.write('\n')

for gene in g2or_New:
	newFile4.write("\t".join(gene))
	newFile4.write('\n')

newFile.close()
newFile2.close()
newFile3.close()
newFile4.close()
