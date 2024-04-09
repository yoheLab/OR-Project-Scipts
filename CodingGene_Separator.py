import os

codingList = list()
pseudoList = list()

with open("T2T_ORA_ORs_Only.korff") as fh:
	for line in fh:
		if line.startswith("Identifier"):
			continue
		else:
			line = line.strip('\n')
			line = line.split('\t')

			if line[7] == "PSEUDOGENE":
				pseudoList.append('\t'.join(line) + '\n')
			elif line[7] == "CODING":
				codingList.append('\t'.join(line) + '\n')

codingFile = open("T2T_ORA_ORs_Only_Coding.korff", "w")
codingFile.write("Identifier	Source	Chromosome	Start	End	Sense	Class	CodingStatus	Sequence	Attribute")
codingFile.write('\n')

for line in codingList:
	codingFile.write(line)

codingFile.close()


pseudoFile = open("T2T_ORA_ORs_Only_Pseudo.korff", "w")
pseudoFile.write("Identifier	Source	Chromosome	Start	End	Sense	Class	CodingStatus	Sequence	Attribute")
pseudoFile.write('\n')

for line in pseudoList:
	pseudoFile.write(line)

pseudoFile.close()