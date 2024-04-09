import os

for file in os.listdir():
	if file.endswith(".korff"):
		dataList = list()
		with open(file) as fh:
			for line in fh:
				if line.startswith("Identifier"):
					continue
				else:
					line = line.strip('\n')
					line = line.split('\t')
					dataList.append(line)

		newFile = open(file + ".fasta", "w")
		for line in dataList:
			newFile.write('>' + line[0] + '\n')
			newFile.write(line[8] + '\n')

		newFile.close()