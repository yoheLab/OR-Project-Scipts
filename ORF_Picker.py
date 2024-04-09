import os

for file in os.listdir():
	if file.endswith(".trimmed"):

		data = list()

		tempHeader = ""
		tempSeq = ""

		with open(file) as fh:
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

		pickedList = list()
		geneIDList = list()

		for entry in data:
			header = entry[0]
			header = header.strip('\n')
			header = header.split("|")
			header = header[1].split(":")
			geneID = header[0]

			if geneID not in geneIDList:
				geneIDList.append(geneID)
				pickedList.append(tuple([geneID, entry[1]]))
			else:
				continue

		newFile = open(file + ".picked", "w")

		for entry in pickedList:
			newFile.write('>' + entry[0] + '\n')
			newFile.write(entry[1] + '\n')

		newFile.close()