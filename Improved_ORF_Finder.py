import os
import sys
import time



def main():

	#list to hold incoming data
	data = list()

	#string to hold target file name
	targetFile = ""
		
	#input handler
	while True:
		try:
			print("Enter Query File: ")
			queryFile = input()
			if targetFile not in os.listdir():
				raise ValueError
			else:
				pass
		except ValueError:
			print("File not found")
		except FileNotFoundError:
			print("File not found")
		else:
			break

	#read in data
	data = fileReadIn(targetFile)

	for entry in data:
		#move values into holder vars
		header = entry[0]
		gene = entry[1]
		


def fileReadIn(targetFile):
	data = list()
	tempHeader = ""
	tempSeq = ""
	progress = 1
	fileLength = 0
	#prime counter
	with open(targetFile) as fh:
		for line in fh:
			fileLength += 1

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
			progress += 1
	data.append(tuple([tempHeader, tempSeq]))
	tempHeader = ""
	tempSeq = ""
	return(data)

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