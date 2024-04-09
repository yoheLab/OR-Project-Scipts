import os

def main():

	data = list()

	tempHeader = ""
	tempSeq = ""

	#need to do this for both
	#change filenames manually
	#also cahnge name of output file at end of program
	with open("g2or_Anno_Merged_ORA.fasta") as fh:
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

	parsedHeaders = list()

	counter = 1

	for tup in data:

		tempHeader = tup[0]

		ident = "G2OR_ANNO" + str(counter)

		source = "G2OR_PIPELINE_ANNO"

		chromosome = ""

		start = ""

		end = ""

		sense = ""

		orClass = ""

		ORA_Coding_Status = ""

		g2or_CODING_Status = ""

		sequence = tup[1]

		attribute = ""

		tempHeader = tempHeader.split(";")

		chromosome = tempHeader[0]
		start = tempHeader[1]
		end = tempHeader[2]
		sense = tempHeader[3]

		tempHeader = tempHeader[5]

		tempHeader = tempHeader.split("|")

		orClass = tempHeader[1]

		if len(tempHeader) == 3:
			ORA_Coding_Status = tempHeader[2]
			g2or_CODING_Status = tempHeader[0]
		elif len(tempHeader) == 2:
			ORA_Coding_Status = "CODING"
			g2or_CODING_Status = tempHeader[0]

		if g2or_CODING_Status == "PSEUDO" and ORA_Coding_Status == "CODING":
			attribute += "Disagree;ORA=C;g2or=P;"
		elif g2or_CODING_Status == "CODING" and ORA_Coding_Status == "PSEUDOGENE":
			attribute += "Disagree;ORA=P;g2or=C;"

		seqLength = len(sequence)

		cordLength = abs(int(start) - int(end))

		if seqLength != cordLength:
			attribute += "ORA_FRAME_SHIFT;"

		parsedHeaders.append(tuple([ident, source, chromosome.lstrip(">"), start, end, sense, orClass, ORA_Coding_Status, sequence, attribute]))

		counter += 1

	newFile = open("T2T_g2or_Anno.korff", "w")
	tab = '\t'
	newFile.write("Identifier" + tab + "Source" + tab + "Chromosome" + tab + "Start" + tab + "End" + tab + "Sense" + tab + "Class" + tab + "CodingStatus" + tab + "Sequence" + tab + "Attribute" + '\n')
	for column in parsedHeaders:
		newFile.write('\t'.join(column) + '\n')
		print('\t'.join(column) + '\n')


	newFile.close()






if __name__ == '__main__':
	main()


# >NC_060938.1 ; 14373999 ; 14374903 ; + ; INTER ; PSEUDO|OR11|PSEUDOGENE