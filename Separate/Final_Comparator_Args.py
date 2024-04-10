import os
import sys

def main():

	#file whos excess genes will be reported
	mainFile = ""
	#file whos genes will be used to elimante duplicates from mainFile
	compareFile = ""

	arguments = sys.argv
	mainFile = arguments[1]
	compareFile = arguments[2]

	#read files into lists
	mainList = tabFileReadIn(mainFile)
	compareList = tabFileReadIn(compareFile)

	#holds the counts for each run in the format:
	#Limit, Coding, Pseudo, Total
	countsList = list()

	#define list to hold all genes that are not removed in the collision
	remainList = list()

	#collide by sequence identity
	remainList = seqCollide(mainList, compareList)

	for i in range(0, 151):
		print("Working on run " + str(i))
		testList = coordCollide(remainList, compareList, i)

		#vars to hold tallys of each gene type
		codingTally = 0
		pseudoTally = 0

		#count up coding and pseudo
		for item in testList:
			if item[7] == "CODING":
				codingTally += 1
			elif item[7] == "PSEUDOGENE":
				pseudoTally += 1
		#add counts to list
		countsList.append(tuple([i, codingTally, pseudoTally, len(testList)]))
	#for item in countsList:
		#print(item)

	#write out counstlist for graphing
	newFile = open("CountsList.csv", "w")
	newFile.write("Minimum Distance, Coding Counts, Pseudo Counts, Total Counts")
	newFile.write('\n')
	for item in countsList:
		newFile.write(str(item[0]) + ", " + str(item[1]) + ", " + str(item[2]) + ", " + str(item[3]))
		newFile.write('\n')
	newFile.close()

	#close program
	exit()

#method to read in tab delimited data
def tabFileReadIn(targetFile):
	#list variable to hold data as it is read in
	dataList = list()
	#open file
	with open(targetFile) as fh:
		for line in fh:
			#strip newlines and split data by tabs
			line = line.strip('\n')
			line = line.split('\t')
			#add line to list
			dataList.append(line)
	#return data to main method
	return(dataList)

#method to confirm all gene identifiers are unique
def uniqueCheck(inputList):
	#list to hold inputList contents during checking procedures
	#holderList defines a position in memeory that will be cleared and reused for multiple purposes
	#this elimnates the need to define more than 2 lists
	holderList = list()
	#truncate list down to just identifiers, use holder list to hold oputput until the two list variables can be swapped
	for item in inputList:
		holderList.append(item[0])
	#set inputList equal to the truncated version 
	inputList = holderList
	#clear holderList memory so it can be used in next step
	holderList.clear()

	#check if any ids are duplicated
	#for each id in the list
	for i in range(0, len(inputList)):
		#counter varialbe to hold the number of id occurences, get automatically reset each time the outer loop iterates
		idCounter = 0
		#check the entire list and add up the number of times the id is present
		for j in range(0, len(inputList)):
			#check if id at position i matches id at position j
			if inputList[i] == inputList[j]:
				#add one to occurence counter
				idCounter += 1
		#add occurence tally to holderList, the occurence tally of each id will be in the same index in holder list as it is in inputList
		holderList.append(idCounter)

	#boolean var to hold result of analysis
	allUnique = True

	#check if any ids have a tally greater than 1
	for tally in holderList:
		if tally > 1:
			#change boolean as not all ids are unique
			allUnique = False

	#return wether all ids in teh input list were unique
	return(allUnique)

#method to remove exact sequence matches 
def seqCollide(mainList, compareList):
	#list to hold all the ids of the genes which remain after collision
	#since ids are confirmed to be unique, they can be used to reference the rest of the gene data later
	IDList = list()
	
	#prime with all mainList ids
	for item in mainList:
		IDList.append(item[0])

	#remove all gene IDs from IDList that occur in both mainList and compareList
	for i in range(0, len(mainList)):
		for j in range(0, len(compareList)):
			#sequence is always at index 8 in a .korff file
			#compare the sequences for 100% identity
			if mainList[i][8] == compareList[j][8]:
				#remove coresponding ID in IDList
				IDList.remove(mainList[i][0])

	#define list to hold full data entries for all remaining genes
	remainList = list()

	#retreive full data for all remianing gene IDs and ad them to remainList
	for ID in IDList:
		for item in mainList:
			if ID == item[0]:
				remainList.append(item)

	#return all remianing genes to main method as a list
	return(remainList)

#method to remove near coordinate matches
def coordCollide(mainList, compareList, limit):
	#list to hold all the ids of the genes which remain after collision
	#since ids are confirmed to be unique, they can be used to reference the rest of the gene data later
	IDList = list()

	#prime with all mainList ids
	for item in mainList:
		IDList.append(item[0])

	#remove all gene IDs from IDList whose coordinates are too close
	for i in range(0, len(mainList)):
		for j in range(0, len(compareList)):
			#move coords in variables to make code more readable
			#coords are always at indexes 3 and 4 in .korff format
			start_1 = int(mainList[i][3])
			end_1 = int(mainList[i][4])
			start_2 = int(compareList[j][3])
			end_2 = int(compareList[j][4])

			#record sense of genes to prevent cross sense comparison
			#sense is always at index 5 in .korff format
			sense_1 = mainList[i][5]
			sense_2 = compareList[j][5]

			#determine if genes are of the same sense and can be compared
			if sense_1 == sense_2:
				#calculate coordinate distances
				#variables to hold calculated distances
				startDistance = abs(start_1 - start_2)
				endDistance = abs(end_1 - end_2)

				#remove gene ID from ID list if coords are too close
				if ((startDistance <= limit) and (endDistance <= limit)):
					#check if ID has already been removed from list
					if mainList[i][0] not in IDList:
						pass
					else:
						#remove coresponding ID in IDList
						IDList.remove(mainList[i][0])

	#define list to hold full data entries for all remaining genes
	remainList = list()

	#retreive full data for all remianing gene IDs and ad them to remainList
	for ID in IDList:
		for item in mainList:
			if ID == item[0]:
				remainList.append(item)

	#return all remianing genes to main method as a list
	return(remainList)

#method to write remaing genes back out in .korff format
def korffWriteOut(remainingList, mainFile, compareFile):
	#trim file names
	mainFile = mainFile.split('.')
	mainFile = mainFile[0]
	compareFile = compareFile.split('.')
	compareFile = compareFile[0]

	#open new file with appropriate name
	newFile = open(mainFile + "_vs_" + compareFile + ".korff", "w")
	for item in remainingList:
		item = "\t".join(item)
		item += "\n"
		newFile.write(item)

	#clsoe new file
	newFile.close()

if __name__ == '__main__':
	main()
