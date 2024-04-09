seenList = list()
with open("T2T_JHU_Anno.gff3") as fh:
	for line in fh:
		line = line.split("\t")
		if line[0] not in seenList:
			seenList.append(line[0])

for item in seenList:
	print(item)