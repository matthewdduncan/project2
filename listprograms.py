##ensure correct: start with ATG, 6 starts on ATG goes to TAA.  1 ends on TGA starts ATG
genome = open('genome.txt', 'r')
table = open('table.txt', 'r')
outfile = open('outfile.txt', 'w')
newgene = ''
gene = ''
genseq = ''
start = True

for line in genome:
	if '>' not in line:
		genseq =genseq + (line.lstrip().rstrip())

for line in table: ##deal with first line
	newgene = ''
	gene = ''
	if start:
		start = False
		continue
	lineinfo = line.split('\t')
	outfile.write(lineinfo[7] + '\t')
	gene = genseq[int(lineinfo[2])-1:int(lineinfo[3])] ##check for off by 1
	
	if '-' in lineinfo[4]:
		for letter in gene[::-1]:
			if letter == 'G':
				nletter = 'C'
			if letter == 'C':
				nletter = 'G'
			if letter == 'A':
				nletter = 'T'
			if letter == 'T':
				nletter = 'A'
			newgene = newgene + nletter
		gene = newgene
	
	outfile.write(gene + '\n')