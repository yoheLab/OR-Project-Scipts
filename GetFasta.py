dataList = list()
seqList = list()
chrSeq = ""
with open("OR2L13_chemo.tblastn.merged.chemo.output.gff3.name") as fh:
	for line in fh:
		line = line.strip("\n")
		line = line.split("\t")
		dataList.append(line)

counter = 0
for data in dataList[0]:
	print(str(counter) + " " + data)
	counter += 1

with open("OR2L13.fasta") as fh:
	for line in fh:
		if line.startswith("A"):
			chrSeq = line.strip("\n")

for data in dataList:
	start = int(data[3])
	end = int(data[4])
	print(start)
	print(end)
	seq = chrSeq[start:end]

	header = ">OR_HIT" + ";" + str(start) + ";" + str(end) + ";"

	seqList.append(tuple([header, seq]))

newFile = open("OR2L13_Found_Seqs.fasta", "w")

for entry in seqList:
	newFile.write(entry[0])
	newFile.write("\n")
	newFile.write(entry[1])
	newFile.write("\n")



newFile.close()




