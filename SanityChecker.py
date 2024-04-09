sequence = "ATGAAGAATGTCACTGAAGTTACCTTATTTGTACTGAAGGGCTTCACAGACAATCTTGAACTGCAGATTATCTTCTTCTTCCTGTTTTTAGCAATCTACCTCTTCACTCTCATGGGAAATTTAGGACTGATTTTACTGGTCATTAGGGATTCCCAGCTCCACAAACCCATGTACTATTTTCTGAGTATGTTGTCTTCTGTGGATGCCTGCTATTCCTCAGTTATTACCCCAAATATGTTAGTAGATTTTACGACAAAGAATAAAGTCATTTCATTCCTTGGATGTGTAGCACAGGTGTTTCTTGCTTGTAGTTTTGGAACCACAGAATGCTTTCTCTTGGCTGCAATGGCTTATGATCGCTATGTAGCCATCTACAACCCTCTCCTGTATTCAGTGAGCATGTCACCCAGAGTCTACATGCCACTCATCAATGCTTCCTATGTTGCTGGCATTTTACATGCTACTATACATACAGTGGCTACATTTAGCCTATCCTTCTGTGGAGCCAATGAAATTAGGCGTGTCTTTTGTGATATCCCTCCTCTCCTTGCTATTTCTTATTCTGACACTCACACAAACCAGCTTCTAGTCTTCTACTTTGTGGGCTCTATCGAGCTGGTCACTATCCTGATTGTTCTGATCTCCTATGGTTTGATTCTGTTGGCCATTCTGAAGATGTATTCTGCTGAAGGGAGGAGAAAAGTCTTCTCCACATGTGGAGCTCACCTAACTGGAGTGTCAATTTATTATGGGACAATCCTCTTCATGTATGTGAGACCAAGTTCCAGCTATGCTTCGGACCATGACATGATAGTGTCAATATTTTACACCATTGTGATTCCCTTGCTGAATCCCGTCATCTACAGTTTGAGGAACAAAGATGTAAAAGACTCAATGAAAAAAATGTTTGGGAAAAATCAGGTTATCAATAAAGTATATTTTCATACTAAAAAATAA"
print("FORWARD:")
print(sequence)
print('\n')
seqList = list(sequence)
compSeq = list()
for base in seqList:
	if base == "A":
		compSeq.append("T")
	elif base == "T":
		compSeq.append("A")
	elif base == "C":
		compSeq.append("G")
	elif base == "G":
		compSeq.append("C")
print("COMPLIMENTARY:")
print("".join(compSeq))
print('\n')
reverse = "".join(compSeq)
reverse = reverse[::-1]
print("REVERSE:")
print(reverse)
print('\n')

data = list()

tempHeader = ""
tempSeq = ""

with open("GCF_009914755.1_T2T-CHM13v2.0_genomic.fna") as fh:
	for line in fh:
		line = line.strip("\n")
		if line.startswith(">"):
			print("Loading Chromosome: " + line + '\n')
			if tempSeq == "":
				tempHeader = line
			elif tempSeq != "":
				data.append(tuple([tempHeader, tempSeq]))
				tempHeader = line
				tempSeq = ""
		else:
			tempSeq += line
data.append(tuple([tempHeader, tempSeq]))
tempHeader = ""
tempSeq = ""

for entry in data:
	if entry[0].startswith(">NC_060935.1"):
		chromoSeq = list(entry[1])
		tempSeq = chromoSeq[56170459:56171415]
		
print('\n')
print("SEQUENCE AT CORDS:")
print(tempSeq)
print('\n')



#ORA7	ORA_PIPELINE	NC_060935.1	56170459	56171415	-	OR5	CODING	ATGAAGAATGTCACTGAAGTTACCTTATTTGTACTGAAGGGCTTCACAGACAATCTTGAACTGCAGATTATCTTCTTCTTCCTGTTTTTAGCAATCTACCTCTTCACTCTCATGGGAAATTTAGGACTGATTTTACTGGTCATTAGGGATTCCCAGCTCCACAAACCCATGTACTATTTTCTGAGTATGTTGTCTTCTGTGGATGCCTGCTATTCCTCAGTTATTACCCCAAATATGTTAGTAGATTTTACGACAAAGAATAAAGTCATTTCATTCCTTGGATGTGTAGCACAGGTGTTTCTTGCTTGTAGTTTTGGAACCACAGAATGCTTTCTCTTGGCTGCAATGGCTTATGATCGCTATGTAGCCATCTACAACCCTCTCCTGTATTCAGTGAGCATGTCACCCAGAGTCTACATGCCACTCATCAATGCTTCCTATGTTGCTGGCATTTTACATGCTACTATACATACAGTGGCTACATTTAGCCTATCCTTCTGTGGAGCCAATGAAATTAGGCGTGTCTTTTGTGATATCCCTCCTCTCCTTGCTATTTCTTATTCTGACACTCACACAAACCAGCTTCTAGTCTTCTACTTTGTGGGCTCTATCGAGCTGGTCACTATCCTGATTGTTCTGATCTCCTATGGTTTGATTCTGTTGGCCATTCTGAAGATGTATTCTGCTGAAGGGAGGAGAAAAGTCTTCTCCACATGTGGAGCTCACCTAACTGGAGTGTCAATTTATTATGGGACAATCCTCTTCATGTATGTGAGACCAAGTTCCAGCTATGCTTCGGACCATGACATGATAGTGTCAATATTTTACACCATTGTGATTCCCTTGCTGAATCCCGTCATCTACAGTTTGAGGAACAAAGATGTAAAAGACTCAATGAAAAAAATGTTTGGGAAAAATCAGGTTATCAATAAAGTATATTTTCATACTAAAAAATAA	NULL