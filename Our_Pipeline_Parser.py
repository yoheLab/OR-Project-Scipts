import os

def main():
	
	data = list()

	tempHeader = ""
	tempSeq = ""

	with open("T2T_Data_Preserved.fasta") as fh:
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

	headerList = list()
	for entry in data:
		headerList.append(entry[0])

	parsedHeaders = list()
	seqCounter = 0
	counter = 1
	for header in headerList:
		print("1")
		print(header)

		ident = "ORA" + str(counter)
		source = "ORA_PIPELINE"
		chromosome = ""
		start = ""
		end = ""
		sense = ""
		orClass = ""
		codingStatus = ""
		attribute = "N/A"

		tempHeader = header

		tempHeader = tempHeader.split(";")
		print("2")
		print(tempHeader)

		chromosome = tempHeader[2].lstrip("Chromosome=")
		start = tempHeader[3].lstrip("Start=")
		end = tempHeader[4].lstrip("End=")

		sense = tempHeader[5].split("|")

		if len(sense) == 2:
			orClass = sense[1]
			codingStatus = "CODING"
		elif len(sense) == 3:
			orClass = sense[1]
			codingStatus = "PSEUDOGENE"

		sense = sense[0]

		if sense == "Sense=-(-)":
			sense = "-"
		elif sense == "Sense=+(+)":
			sense = "+"

		parsedHeaders.append(tuple([ident, source, chromosome, start, end, sense, orClass, codingStatus, data[seqCounter][1], attribute]))
		seqCounter += 1
		counter += 1

	for header in parsedHeaders:
		print(header)

	newFile = open("T2T_ORA.korff", "w")
	tab = '\t'
	newFile.write("Identifier" + tab + "Source" + tab + "Chromosome" + tab + "Start" + tab + "End" + tab + "Sense" + tab + "Class" + tab + "CodingStatus" + tab + "Sequence" + tab + "Attribute" + '\n')
	for column in parsedHeaders:
		newFile.write('\t'.join(column) + '\n')


	newFile.close()


if __name__ == '__main__':
	main()

#>ID=V1R_XP_001488721.2.match_part63 ; Target=V1R_XP_001488721.2 ; Chromosome=NC_060931.1 ; Start=65358045 ; End=65358359 ; Sense=-(-)|V1R|PSEUDOGENE