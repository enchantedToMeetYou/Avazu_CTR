from itertools import izip

with open("submissionCombined.csv","w") as outfile:	
	outfile.write("id,click\n")
	with open("submission.csv","r") as inputfile1, open("submissionFV.csv","r") as inputfile2:
		inputfile1.next()
		inputfile2.next()
		for line1, line2 in izip(inputfile1, inputfile2):	
			rowFile1 = line1.strip().split(",")
			rowFile2 = line2.strip().split(",")
			outfile.write("%s,%f\n"%(rowFile1[0],(float(rowFile1[1])+float(rowFile2[1]))/2))
