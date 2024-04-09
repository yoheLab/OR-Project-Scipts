import os

def main():

	

	for file in os.listdir():
		#print(file)
		if file.endswith(".output.gff3"):
			newFile = open(file + ".info", "w")
			#print("Writing File " + file + ".info")
			with open(file) as fh:
				for line in fh:
					#print(line)
					line = line.split("	")
					#print(line)
					#chromosome, start, end, sense
					attribute = line[8]
					#print(attribute)
					attribute = attribute.split(" ")
					#chromosome
					attribute[0] += ";Chromosome=" + line[0]
					#start
					attribute[0] += ";Start=" + line[3]
					#end
					attribute[0] += ";End=" + line[4]
					#sense
					attribute[0] += ";Sense=" + line[6]

					attribute = " ".join(attribute)
					#print(attribute)

					newLine = line[0] + "\t" + line[1] + "\t" +line[2] + "\t" +line[3] + "\t" +line[4] + "\t" +line[5] + "\t" +line[6] + "\t" + line[7] + "\t" + attribute
					#print(newLine)

					newFile.write(newLine)
			newFile.close()


if __name__ == '__main__':
	main()