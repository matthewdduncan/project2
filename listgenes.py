genome = open('genome.txt', 'r')
table = open('table.txt', 'r')
outfile = open('genelist.txt', 'w')
newgene = ''
gene = ''
genseq = ''
start = True

#get string of genome
for line in genome:
	if '>' not in line:
		genseq =genseq + (line.lstrip().rstrip())

#write new file
for line in table:
	newgene = ''
	gene = ''
	if start:  ## skip first line
		start = False
		continue
	lineinfo = line.split('\t')
	outfile.write(lineinfo[7] + '\t') ## get protein name
	gene = genseq[int(lineinfo[2])-1:int(lineinfo[3])]
	
	#Handle reverse strand
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
	
	#write the gene
	outfile.write(gene + '\n')