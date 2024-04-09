import os
import time

#target is declared as a global variable to cut down on read/write operations in ram
target = ""
#global average time varaible so all methods can easily access it


def main():

	queryFile = ""
	targetFile = ""

	
		
	#query input handler
	while True:
		try:
			print("Enter Query File: ")
			queryFile = input()
			if queryFile not in os.listdir():
				raise ValueError
			else:
				pass
		except ValueError:
			print("File not found")
		except FileNotFoundError:
			print("File not found")
		else:
			break
		
	#target input handler
	while True:
		try:
			print("Enter Target File: ")
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

	#start timer
	start = time.time()

	#read in query file
	queryList = list()
	targetList = list()
	print('\n')
	print("Reading in " + queryFile)
	#print("Time Elapsed: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))
	#print('\n')
	queryList = fileReadIn(queryFile, start)
	print('\n')
	print("Reading in " + targetFile)
	#print("Time Elapsed: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))
	#print('\n')
	targetList = fileReadIn(targetFile, start)
	print('\n')

	#list to hold all alignment data
	alignList = list()
	#temp list to hold each round of data from the alignment method unitl it is added to the main list
	tempList = list()

	#variable to track progress throguh chromosomes
	chrProgress = 1

	#for each chromosome/sequence in in the genome/target file
	for entry in targetList:
		print("Aligning Chromosome " + str(chrProgress) + " of " + str(len(targetList)))
		#print("Time Elapsed: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))
		#print('\n')
		#global variable target is set equal to each chromosome in the genome
		global target
		target = entry[1]


		#variable to track progress through queries
		queryProgress = 1

		#initialize time variable for first run
		alignEnd = 0
		#for each sequence in the query file
		for query in queryList:
			alignStart = time.time()
			print_progress(queryProgress, len(queryList), alignStart, alignEnd)
			alignEnd = time.time()
			#pass variables into align method
			tempList = align(query[1], query[0], entry[0])
			#update sequence progress counter
			queryProgress += 1
			#move data from tempList into main list
			for tempData in tempList:
				#print(tempData)
				alignList.append(tempData)
			#dump tempList memory
			tempList.clear()
		#update chromosome progress counter
		chrProgress += 1
		#extra space to make things look nice and readable
		print('\n')

	#write all alignment data to a file
	print('\n')
	print("Writing Alignments File")
	print("Time Elapsed: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))
	#trim file names to remove extensions
	queryFile = queryFile.split(".")
	queryFile = queryFile[0]
	targetFile = targetFile.split(".")
	targetFile = targetFile[0]
	newFile = open(queryFile + "_aligned_to_" + targetFile + ".align", "w")
	for entry in alignList:
		newFile.write("\t".join(entry))
		newFile.write("\n")
	newFile.close()



def fileReadIn(targetFile, start):
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
			print_load_progress(progress, fileLength, start)
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

def align(query, queryHeader, targetHeader):
	#print("Method Starts")
	#list to hold all the alignment data
	hitList = list()
	#generate reverse compliment
	antiQuery = ""
	tempSeqHolder = list(query)
	for base in tempSeqHolder:
		if base == "A":
			antiQuery += "T"
		elif base == "T":
			antiQuery += "A"
		elif base == "C":
			antiQuery += "G"
		elif base == "G":
			antiQuery += "C"
	antiQuery = antiQuery[::-1]

	#variable to reference sequence lenghts and make things readable
	targetLength = len(target)
	queryLength = len(query)

	#search for sense + sense genes
	for i in range(0, targetLength):
		#check if out of range
		if ((queryLength - 1) + i) > (targetLength - 1):
			break
		else:
			#print("Checking " + targetHeader + " in range " + str(i) + " to " + str(i + queryLength))
			subTarget = target[i:(i + queryLength)]
			#print(subTarget)
			if query == subTarget:
				hitList.append(tuple([queryHeader, query, targetHeader, str(i), str(i + queryLength), "+"]))
	#search for - sense genes
	for i in range(0, targetLength):
		#check if out of range
		if ((queryLength - 1) + i) > (targetLength - 1):
			break
		else:
			subTarget = target[i:(i + queryLength)]
			if antiQuery == subTarget:
				hitList.append(tuple([queryHeader, query, targetHeader, str(i), str(i + queryLength), "-"]))
	#return all hits
	return(hitList)

def print_progress(x, y, alignStart, alignEnd):
    print(f"Aligning query {x} out of {y} | " + averageRunningTime(alignStart, alignEnd), end="\r", flush=True)

def print_load_progress(progress, fileLength, start):
    # Calculate the number of characters to represent the progress bar
    progress_chars = int(progress / fileLength * 50)
    # Create the progress bar string
    progress_bar = "[" + "=" * progress_chars + " " * (50 - progress_chars) + "]"
    # Print the progress bar on the same line with carriage return (\r)
    print(f"\r{progress_bar} {progress}/{fileLength} | " + timeElapsed(start), end="", flush=True)

def timeElapsed(start):
	return("Time Elapsed: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))

def averageRunningTime(alignStart, alignEnd):
	return("Last Alignment took: " + time.strftime("%H:%M:%S", time.gmtime(alignEnd - alignStart)))

















if __name__ == '__main__':
	main()
