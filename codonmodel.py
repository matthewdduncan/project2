import math

infile = open('genelist.txt')
output = open('finalCUI.txt', 'w')
outtable = open('codontable.txt', 'w')

codon = ''
allgenescodons = {}
codonsingene = []
totalcodons= []
codonfreqtotal = {}

## Find all codons in all genes
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
			
# Find frequencies of each codon
for codon in totalcodons:
	if codon not in codonfreqtotal.keys():
		codonfreqtotal[codon] = 1
	else:
		codonfreqtotal[codon] += 1
		
#convert to relative frequency		
for key in codonfreqtotal.keys():
	codonfreqtotal[key] /= len(totalcodons)

#create table header	
for codon in sorted(codonfreqtotal.keys()):
	outtable.write(codon + '\t')

#compute frequency and relative frequency per gene.	
for gene in allgenescodons.keys():
	sum = 0
	codonfreqgene = {}
	for codon in allgenescodons[gene]:
		if codon not in codonfreqgene.keys():
			codonfreqgene[codon] = 1
		else:
			codonfreqgene[codon] += 1
		
	outtable.write('\n')
	
	# put numbers in table, alphabetically by codon
	for codon in sorted(codonfreqtotal.keys()):
		if codon in codonfreqgene.keys():
			outtable.write(str(codonfreqgene[codon]) + '\t')
		else:
			outtable.write('0' + '\t')
	
	#count stop codons
	outtable.write(str(codonfreqgene.get('TAA',0) + codonfreqgene.get('TAG',0) + codonfreqgene.get('TGA',0)))
	
	# have no use for true frequency after table is made, so convert to rlative
	for codon in codonfreqgene.keys():
		codonfreqgene[codon] /= len(allgenescodons[gene])
		sum += codonfreqgene[codon] * codonfreqtotal[codon]
	
	output.write(gene + '\t' + str(sum) + '\n')
		