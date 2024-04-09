import os
import sys
import time


def main():

	#declare lists to hold data as it is deduplicated
	data = list()
	dedupeData = list()
	dupeData = list()

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

	#read in data into first list
	data = fileReadIn(fileName)

	#list to hold duplicated sequences
	dupeSeqs = list()

	#dedupe by sequence
	# for i in range(0, len(data)):
	# 	sequence = data[i][1]
	# 	#calculate reverse compliment to check other strand
	# 	antiSequence = reverseCompliment(sequence)
	# 	#reset dupe boolean before checking again
	# 	dupe = False
	# 	for j in range(0, len(data)):
	# 		#make sure it doesnt count entry i as a dupe of itself
	# 		if j == i:
	# 			continue
	# 		else:
	# 			if (sequence == data[j][1]) or (antiSequence == data[j][1]):
	# 				dupe = True
	# 	if dupe == True:
	# 		dupeData.append(data[i])
	# 	elif dupe == False:
	# 		dedupeData.append(data[i])

	for entry in data:
		sequence = entry[1]
		#calculate reverse compliment to check other strand
		antiSequence = reverseCompliment(sequence)
		if (sequence not in dupeSeqs) and (antiSequence not in dupeSeqs):
			dedupeData.append(entry)
			dupeSeqs.append(sequence)
			dupeSeqs.append(antiSequence)

	print("Data :" + str(len(data)))
	print("Dedupe :" + str(len(dedupeData)))
	print("Dupe :" + str(len(dupeData)))

	#write out dupe and dedupe data
	writeToFasta(dedupeData, "Dedupe")
	writeToFasta(dupeData, "Dupe")


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

def writeToFasta(fastaData, fileName):

	#open new file with name based off of read in file
	newFile = open(fileName + ".fasta", "w")

	#write data into new file
	for entry in fastaData:
		newFile.write(entry[0])
		newFile.write('\n')
		newFile.write(entry[1])
		newFile.write('\n')

	#close new file before ending
	newFile.close()

def reverseCompliment(forwardGene):
	#variable to hold the antiGene as it is created
	antiGene = ""

	#reverse forward gene
	reverseGene = forwardGene[::-1]

	#find complimentary bases of reversed gene
	for base in reverseGene:
		if base == "A":
			antiGene += "T"
		elif base == "T":
			antiGene += "A"
		elif base == "C":
			antiGene += "G"
		elif base == "G":
			antiGene += "C"

	#retrun reverse compliment
	return(antiGene)

if __name__ == '__main__':
	main()