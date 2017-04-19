import math

infile = open('genelist.txt')
output = open('finalCUI.txt', 'w')
outtable = open('codontable.txt', 'w')

codon = ''
allgenescodons = {}
codonsingene = []
totalcodons= []
codonfreqtotal = {}

for line in infile:
	codonsingene = []
	seq = line.split('\t')
	codon = ''
	if len(seq[1].rstrip()) % 3 != 0:
		continue
	for ch in seq[1].rstrip():
		codon += ch
		if len(codon) == 3:
			codonsingene.append(codon)
			totalcodons.append(codon)
			codon = ''
	allgenescodons[seq[0].lstrip().rstrip()] = codonsingene
			
for codon in totalcodons:
	if codon not in codonfreqtotal.keys():
		codonfreqtotal[codon] = 1
	else:
		codonfreqtotal[codon] += 1
		
for key in codonfreqtotal.keys():
	codonfreqtotal[key] /= len(totalcodons)
	
for codon in sorted(codonfreqtotal.keys()):
	outtable.write(codon + '\t')
	
for gene in allgenescodons.keys():
	sum = 0
	codonfreqgene = {}
	for codon in allgenescodons[gene]:
		if codon not in codonfreqgene.keys():
			codonfreqgene[codon] = 1
		else:
			codonfreqgene[codon] += 1
		
	outtable.write('\n')
	
	for codon in sorted(codonfreqtotal.keys()):
		if codon in codonfreqgene.keys():
			outtable.write(str(codonfreqgene[codon]) + '\t')
		else:
			outtable.write('0' + '\t')
			
	outtable.write(str(codonfreqgene.get('TAA',0) + codonfreqgene.get('TAG',0) + codonfreqgene.get('TGA',0)))
	
	for codon in codonfreqgene.keys():
		codonfreqgene[codon] /= len(allgenescodons[gene])
		sum += codonfreqgene[codon] * codonfreqtotal[codon]
	
	output.write(gene + '\t' + str(sum) + '\n')
		