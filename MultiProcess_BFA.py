import os
import time
import multiprocessing

#list to hold all alignment data, list is global so threads can access it
alignList = list()

def main():

	queryFile = ""
	targetFile = ""

	#define a lock to allow all threads to write to the same global list
	lock = threading.Lock()

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
	print("Time Elapsed: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))
	print('\n')
	queryList = fileReadIn(queryFile)
	#make queryList divisible by 4
	while True:
		if (4 % len(queryList)) != 0:
			queryList.append(tuple(">FILLER SEQ", "Z"))
		else:
			break

	print('\n')
	print("Reading in " + targetFile)
	print("Time Elapsed: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))
	print('\n')
	targetList = fileReadIn(targetFile)
	print('\n')


	#temp list to hold each round of data from the alignment method unitl it is added to the main list
	tempList = list()

	#variable to track progress throguh chromosomes
	chrProgress = 1

	#for each chromosome/sequence in in the genome/target file
	for entry in targetList:
		print("Aligning Chromosome " + str(chrProgress) + " of " + str(len(targetList)))
		print("Time Elapsed: " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start)))
		print('\n')
		#variable to track progress through queries
		queryProgress = 1

		#for each sequence in the query file
		for i in range(0, len(queryList), 4):
			#print progress
			print_progress(queryProgress, len(queryList))

			#pass variables into threads
			t1 = threading.Thread(target=align, args= (queryList[i][1], entry[1], queryList[i][0], entry[0], lock))
			t2 = threading.Thread(target=align, args= (queryList[i+1][1], entry[1], queryList[i+1][0], entry[0], lock))
			t3 = threading.Thread(target=align, args= (queryList[i+2][1], entry[1], queryList[i+2][0], entry[0], lock))
			t4 = threading.Thread(target=align, args= (queryList[i+3][1], entry[1], queryList[i+3][0], entry[0], lock))

			#START THREADS
			t1.start()
			t2.start()
			t3.start()
			t4.start()
			
			#JOIN THREADS
			t1.join()
			t2.join()
			t3.join()
			t4.join()

			#update sequence progress counter
			queryProgress += 4
		#update chromosome progress counter
		chrProgress += 1

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
			print_load_progress(progress, fileLength)
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

def align(query, target, queryHeader, targetHeader, lock):
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
				lock.aquire()
				alignList.append(tuple([queryHeader, query, targetHeader, str(i), str(i + queryLength), "+"]))
				lock.release()
	#search for - sense genes
	for i in range(0, targetLength):
		#check if out of range
		if ((queryLength - 1) + i) > (targetLength - 1):
			break
		else:
			subTarget = target[i:queryLength]
			if antiQuery == subTarget:
				lock.aquire()
				alignList.append(tuple([queryHeader, query, targetHeader, str(i), str(i + queryLength), "-"]))
				lock.release()
	#end method
	return()

def print_progress(x, y):
    print(f"Aligning query {x} out of {y}", end="\r", flush=True)

def print_load_progress(progress, fileLength):
    # Calculate the number of characters to represent the progress bar
    progress_chars = int(progress / fileLength * 50)
    # Create the progress bar string
    progress_bar = "[" + "=" * progress_chars + " " * (50 - progress_chars) + "]"
    # Print the progress bar on the same line with carriage return (\r)
    print(f"\r{progress_bar} {progress}/{fileLength}", end="", flush=True)





















if __name__ == '__main__':
	main()
