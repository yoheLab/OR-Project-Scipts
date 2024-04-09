with open("T2T_JHU_Anno_ORs.fasta") as fh:
	for line in fh:
		line = line.strip('\n')
		if line.startswith(">"):
			print(line)
		else:
			print(str(len(line)))