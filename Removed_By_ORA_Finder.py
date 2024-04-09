import os

def main():

	data_Pre = list()
	data_Pre_Cord = list()
	data_Post = list()
	data_Post_Cord = list()
	data_Removed = list()

	tempHeader = ""
	tempSeq = ""

	with open("g2or_Anno_Merged.fasta") as fh:
		for line in fh:
			line = line.strip("\n")
			if line.startswith(">"):
				if tempSeq == "":
					tempHeader = line
				elif tempSeq != "":
					data_Pre.append(tuple([tempHeader, tempSeq]))
					tempHeader = line
					tempSeq = ""
			else:
				tempSeq += line


	data_Pre.append(tuple([tempHeader, tempSeq]))
	tempHeader = ""
	tempSeq = ""

	with open("g2or_Anno_Merged_ORA.fasta") as fh:
		for line in fh:
			line = line.strip("\n")
			if line.startswith(">"):
				if tempSeq == "":
					tempHeader = line
				elif tempSeq != "":
					data_Post.append(tuple([tempHeader, tempSeq]))
					tempHeader = line
					tempSeq = ""
			else:
				tempSeq += line


	data_Post.append(tuple([tempHeader, tempSeq]))
	tempHeader = ""
	tempSeq = ""


	for gene in data_Pre:
		temp = gene[0]
		temp = temp.split(";")
		start = temp[1]
		end = temp[2]
		data_Pre_Cord.append(tuple([start, end]))

	for gene in data_Post:
		temp = gene[0]
		temp = temp.split(";")
		start = temp[1]
		end = temp[2]
		data_Post_Cord.append(tuple([start, end]))

	for i in range(0, len(data_Pre_Cord)):
		if data_Pre_Cord[i] not in data_Post_Cord:
			print(str(i))
			print(data_Pre_Cord[i])
			print(data_Pre[i])










if __name__ == '__main__':
	main()