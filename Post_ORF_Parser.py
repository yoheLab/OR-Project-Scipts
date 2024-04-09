import os

for file in os.listdir():
	if file.endswith(".clean.fasta"):
		newFile = open(file + ".korff", "w")
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

		parsedHeaders = list()

		for entry in data:

			header = entry[0]

			identifier = ""
			source = ""
			chromosome = ""
			start = ""
			end = ""
			sense = ""
			orClass = ""
			codingStatus = ""
			attribute = "NULL"

			header = header.split(";")

			#identifier
			identifier = header[0]
			identifier = identifier.split(".")
			identifier = identifier[0]
			identifier = identifier.split("=")
			identifier = identifier[1]

			#source
			if identifier.startswith("ORA"):
				source = "ORA_PIPELINE"
			elif identifier.startswith("G2OR_ANNO"):
				source = "G2OR_PIPELINE_ANNO"
			elif identifier.startswith("G2OR_ITER"):
				source = "G2OR_PIPELINE_ITER"
			else:
				print("ERROR in source")

			#chromosome
			chromosome = header[2]
			chromosome = chromosome.split("=")
			chromosome = chromosome[1]

			#start
			start = header[3]
			start = start.split("=")
			start = start[1]

			#end
			end = header[4]
			end = end.split("=")
			end = end[1]

			#sense + codingStatus + orClass
			sense = header[5]
			sense = sense.split("|")
			if len(sense) == 2:
				codingStatus = "CODING"
			elif len(sense) == 3:
				codingStatus = "PSEUDOGENE"
			else:
				print("ERROR in codingStatus")
			orClass = sense[1]
			sense = sense[0]
			sense = sense.split("=")
			sense = sense[1]
			if sense == "-(-)":
				sense = "-"
			elif sense == "+(+)":
				sense = "+"
			else:
				print("ERROR in sense")

			parsedHeaders.append(tuple([identifier, source, chromosome, start, end, sense, orClass, codingStatus, entry[1], attribute]))

		tab = '\t'
		#newFile.write("Identifier" + tab + "Source" + tab + "Chromosome" + tab + "Start" + tab + "End" + tab + "Sense" + tab + "Class" + tab + "CodingStatus" + tab + "Sequence" + tab + "Attribute" + '\n')

		for header in parsedHeaders:
			newFile.write("\t".join(header) + '\n')

		newFile.close()





#>ID=ORA7.match_part1 ; Target=ORA7 ; Chromosome=NC_060935.1 ; Start=56170459 ; End=56171415 ; Sense=-(-)|OR5