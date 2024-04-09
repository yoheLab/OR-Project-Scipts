import os
import time

def main():

	#name of file to be trimmed
	fileName = ""

	#file input handler
	while True:
		try:
			print("Enter Query File: ")
			fileName = input()
			if fileName not in os.listdir():
				raise ValueError
			else:
				pass
		except ValueError:
			print("File not found")
		except FileNotFoundError:
			print("File not found")
		else:
			break



	#read in file
	geneList = fileReadIn(fileName)

	#trim genes
	trimmedGenes = findORFs(geneList)

	newFile = open(fileName + "_python_ORF.trimmed", "w")
	for gene in trimmedGenes:
		newFile.write(gene[0] + "\n")
		newFile.write(gene[1] + "\n")
	newFile.close()


def fileReadIn(targetFile):
	data = list()
	tempHeader = ""
	tempSeq = ""

	with open(targetFile) as fh:
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
				#make sure all bases are uppercase
				tempSeq += line.upper()
	data.append(tuple([tempHeader, tempSeq]))
	tempHeader = ""
	tempSeq = ""
	return(data)

def findORFs(geneList):
	#file to hold all the trimmed genes
	trimmedGenes = list()



	for gene in geneList:

		#boolean flags to store outcome info
		positiveGeneFound = False
		negativeGeneFound = False

		#variable to hold gene
		tempGene = gene[1]
		#variable to hold reverse compliment gene
		antiGene = ""
		#calculate reverse compliment
		for base in list(tempGene):
			if base == "A":
				antiGene += "T"
			elif base == "T":
				antiGene += "A"
			elif base == "C":
				antiGene += "G"
			elif base == "G":
				antiGene += "C"
		antiGene = antiGene[::-1]

		#search for start codon in + sense
		for i in range(0, len(tempGene)):
			#check if out of range
			if ((3 + i) > (len(tempGene) - 1)):
				break
			else:
				codon = tempGene[i:(i + 3)]
				if codon == "ATG":
					tempGene = tempGene[i:len(tempGene)]

		#search for end codon in + sense
		for i in range(0, len(tempGene), 3):
			#check if out of range
			if ((3 + i) > (len(tempGene) - 1)):
				break
			else:
				codon = tempGene[i:(i + 3)]
				if codon == "TAA" or codon == "TAG" or codon == "TGA":
					tempGene = tempGene[0:(i + 3)]


		#search for start codon in - sense
		for i in range(0, len(antiGene)):
			#check if out of range
			if ((3 + i) > (len(antiGene) - 1)):
				break
			else:
				codon = antiGene[i:(i + 3)]
				if codon == "ATG":
					antiGene = antiGene[i:len(antiGene)]

		#search for end codon in + sense
		for i in range(0, len(antiGene), 3):
			#check if out of range
			if ((3 + i) > (len(antiGene) - 1)):
				break
			else:
				codon = antiGene[i:(i + 3)]
				if codon == "TAA" or codon == "TAG" or codon == "TGA":
					antiGene = antiGene[0:(i + 3)]

		#check to see if a good ORF was found
		if tempGene.startswith("ATG"):
			if tempGene.endswith("TAA") or tempGene.endswith("TAG") or tempGene.endswith("TGA"):
				if len(tempGene) > len(antiGene):
					trimmedGenes.append(tuple([gene[0] + ";Sense=+", tempGene]))
					positiveGeneFound = True
		if antiGene.startswith("ATG"):
			if antiGene.endswith("TAA") or antiGene.endswith("TAG") or antiGene.endswith("TGA"):
				if len(antiGene) > len(tempGene):
					trimmedGenes.append(tuple([gene[0] + ";Sense=-", antiGene]))
					negativeGeneFound = True

		if (positiveGeneFound or negativeGeneFound) != True:
			trimmedGenes.append(tuple([gene[0] + ";Sense=NEITHER", "NULL"]))


	return(trimmedGenes)














if __name__ == '__main__':
	main()