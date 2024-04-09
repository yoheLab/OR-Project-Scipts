counter = 0
newFile = open("T2T_JHU_Anno_ORs.gff3", "w")
newFile2 = open("oddballs.gff3", "w")
with open("T2T_JHU_Anno.gff3") as fh:
	for line in fh:

		if line.startswith("#"):
			continue

		bool_OR = False
		bool_description = False


		holder = line
		line = line.strip('\n')
		line = line.split('\t')

		line = line[8]
		line = line.split(";")

		if line[1].startswith("gene_name=OR"):
			geneName = line[1]
			geneName = geneName.lstrip("gene_name=OR")
			for i in range(1, 15):
				if geneName.startswith(str(i)):
					bool_OR = True

		if line[3].startswith("description=olfactory receptor"):
			bool_description = True

		if bool_OR or bool_description:
			if bool_OR != bool_description:
				newFile2.write(holder)
			counter += 1
			newFile.write(holder)


newFile.close()
newFile2.close()
print("OR Genes Recovered: " + str(counter))
		




#chr1	Liftoff	gene	111940	112877	.	-	.	attribute

#Attribute:

# 0 ID=OR4F29;
# 1 gene_name=OR4F29;
# 2 db_xref=HGNC:HGNC:31275;
# 3 description=olfactory receptor family 4 subfamily F member 29;
# 4 gbkey=Gene;
# 5 gene=OR4F29;
# 6 gene_biotype=protein_coding;
# 7 gene_synonym=OR7-21;
# 8 coverage=0.998;
# 9 sequence_ID=0.989;
# 10 valid_ORFs=0;
# 11 extra_copy_number=0;
# 12 copy_num_ID=OR4F29_0