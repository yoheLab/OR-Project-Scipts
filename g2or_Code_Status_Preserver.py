import os

def main():

	with open("ORannotation_itera5_final_pseu_ORs.fasta") as fh:
		newFile = open("g2or_Iter_Pseu.fasta", "w")

		for line in fh:
			if line.startswith(">"):
				line = line.strip("\n")
				print("EDIT 1")
				print(line)
				
				line = line.split("_")
				print("EDIT 2")
				print(line)

				line = ";".join(line)
				print("EDIT 3")
				print(line)

				line = line.split("@#@")
				print("EDIT 4")
				print(line)

				line = "_".join(line)
				print("EDIT 5")
				print(line)

				line += ";" + "PSEUDO"
				print("EDIT 6")
				print(line)

				line += "\n"

			newFile.write(line)

		newFile.close()

	with open("ORannotation_final_pseu_ORs.fasta") as fh:
		newFile = open("g2or_Anno_Pseu.fasta", "w")

		for line in fh:
			if line.startswith(">"):
				line = line.strip("\n")
				print("EDIT 1")
				print(line)
				
				line = line.split("_")
				print("EDIT 2")
				print(line)

				line = ";".join(line)
				print("EDIT 3")
				print(line)

				line = line.split("@#@")
				print("EDIT 4")
				print(line)

				line = "_".join(line)
				print("EDIT 5")
				print(line)

				line += ";" + "PSEUDO"
				print("EDIT 6")
				print(line)

				line += "\n"

			newFile.write(line)

		newFile.close()

	with open("ORannotation_itera5_final_func_dna_ORs.fasta") as fh:
		newFile = open("g2or_Iter_Coding.fasta", "w")

		for line in fh:
			if line.startswith(">"):
				line = line.strip("\n")
				print("EDIT 1")
				print(line)
				
				line = line.split("_")
				line.pop(0)
				print("EDIT 2")
				print(line)

				line = ";".join(line)
				print("EDIT 3")
				print(line)

				line = line.split("@#@")
				print("EDIT 4")
				print(line)

				line = "_".join(line)
				print("EDIT 5")
				print(line)

				line += ";" + "CODING"
				line = ">" + line
				print("EDIT 6")
				print(line)

				line += "\n"
				

			newFile.write(line)

		newFile.close()

	with open("ORannotation_final_func_dna_ORs.fasta") as fh:
		newFile = open("g2or_Anno_Coding.fasta", "w")

		for line in fh:
			if line.startswith(">"):
				line = line.strip("\n")
				print("EDIT 1")
				print(line)
				
				line = line.split("_")
				line.pop(0)
				print("EDIT 2")
				print(line)



				line = ";".join(line)
				print("EDIT 3")
				print(line)

				line = line.split("@#@")
				print("EDIT 4")
				print(line)

				line = "_".join(line)
				print("EDIT 5")
				print(line)

				line += ";" + "CODING"
				line = ">" + line
				print("EDIT 6")
				print(line)

				line += "\n"


			newFile.write(line)

		newFile.close()








if __name__ == '__main__':
	main()