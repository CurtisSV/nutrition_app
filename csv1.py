import csv

lentil_dict = {}
with open('lentil_protein.txt', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	rowSum = 0
	for row in spamreader:
		rowSum += float(row[2])
		#print row[0] + "," + row[2]
	#print str(rowSum) + " total grams of protein"
	csvfile.seek(0)
	for row in spamreader:
		protein_percentage = round(float(row[2])/rowSum, 3)*100
		lentil_dict[row[0].lower()] = protein_percentage
		#print row[0] + "," + row[2] + "," + str(protein_percentage)

whey_dict = {}
with open("whey_protein.txt") as csvfile:
	spamreader = csv.reader(csvfile, delimiter="\t")
	for row in spamreader:
		whey_dict[row[0].lower()] = float(row[1])
		#print row[0] + "," + row[1]

diffs_dict = {}
for k in lentil_dict.keys():
	diff = whey_dict[k] - lentil_dict[k]
	diffs_dict[k] = k
	print k + str(diff)

#print diffs_dict