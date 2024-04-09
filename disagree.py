import os

def main():

	ORA_P_G2OR_C_NFS = 0

	ORA_C_G2OR_P_NFS = 0

	ORA_P_G2OR_C_FS = 0

	ORA_C_G2OR_P_FS = 0

	Agree_FS = 0

	Pure_Agree = 0


	data = list()

	with open("T2T_g2or_Iter.korff") as fh:
		for line in fh:
			data.append(line.strip('\n'))

	for line in data:

		line = line.split('\t')

		line = line[9]

		if line == "":
			Pure_Agree += 1

		elif line == "ORA_FRAME_SHIFT;":
			Agree_FS += 1

		elif line == "Disagree;ORA=P;g2or=C;":
			ORA_P_G2OR_C_NFS += 1

		elif line == "Disagree;ORA=C;g2or=P;":
			ORA_C_G2OR_P_NFS += 1

		elif line == "Disagree;ORA=P;g2or=C;ORA_FRAME_SHIFT;":
			ORA_P_G2OR_C_FS += 1

		elif line == "Disagree;ORA=C;g2or=P;ORA_FRAME_SHIFT;":
			ORA_C_G2OR_P_FS += 1

	print("ITER")
	print("ORA=P G2OR=C NoFrameShift:")
	print(str(ORA_P_G2OR_C_NFS))
	print("ORA=C G2OR=P NoFrameShift:")
	print(str(ORA_C_G2OR_P_NFS))
	print("ORA=P G2OR=C FrameShift:")
	print(str(ORA_P_G2OR_C_FS))
	print("ORA=C G2OR=P FrameShift:")
	print(str(ORA_C_G2OR_P_FS))
	print("Agree FrameShift:")
	print(str(Agree_FS))
	print("Agree:")
	print(str(Pure_Agree))








if __name__ == '__main__':
	main()


