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
			targetFile = input()
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
	data = tabFileReadIn(targetFile)

	print(len(data))
	counter = 0
	for item in data[1]:
		print(str(counter) + " : " + item)
		counter += 1

	#list to hold data reformated into fasta format
	fastaData = reFormat(data)

	#write data to fasta file
	writeToFasta(fastaData, targetFile)


def tabFileReadIn(fileName):

	#list to hold data until it is passed out of function
	dataHolder = list()
	with open(fileName) as fh:
		for line in fh:
			line = line.strip('\n')
			line = line.lstrip('>')
			line = line.split('\t')
			dataHolder.append(line)

	#retrun data back to main method
	return(dataHolder)

def reFormat(dataList):
	#declare variables to hold data as it is parsed
	identifier = ""
	sequence = ""
	chromosome = ""
	start = ""
	end = ""
	sense = ""



	#declare list to hold parsed data
	parsedData = list()

	for entry in dataList:

		#parse out each value to its variable
		identifier = entry[0]
		sequence = entry[1]
		chromosome = entry[2]
		start = entry[3]
		end = entry[4]
		sense = entry[5]

		#parse chromosome down to its accession number
		chromosome = chromosome.split(" ")
		chromosome = chromosome[0]
		chromosome = chromosome.lstrip(">")

		#create header
		header = ">" + identifier + ";" + chromosome + ";" + start + ";" + end + ";" + sense

		#add data into fasta format list
		parsedData.append(tuple([header, sequence]))

	#return parsed data back to main method
	return(parsedData)

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




















if __name__ == '__main__':
	main()