newFile = open("T2T_ORA_ORs_Only.korff", "w")
with open("T2T_ORA.korff") as fh:
	for line in fh:
		if line.startswith("Identifier"):
			continue
		else:
			line = line.split("\t")
			if line[6].startswith("OR"):
				line = "\t".join(line)
				newFile.write(line)

newFile.close()