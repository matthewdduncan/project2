import numpy
import matplotlib.pyplot as plt

infile = open('finalCUI.txt')

i = 0
scatter1 = []

## get all CUI values
for line in infile:
	scatter1.append(float(line.split('\t')[1])) 
	i += 1
	
s1x = [i for i in range(len(scatter1))]

##plot scatter1
plt.scatter(s1x, scatter1)
plt.ylabel('CUI')
plt.savefig('scatter1.png')

#clear plot to allow for new figure
plt.clf()

##plot scatter2
plt.scatter(s1x, sorted(scatter1))
plt.savefig('scatter2.png')

plt.clf()

plt.hist(scatter1, bins = 10) ## numpy histogram automatically creates 10 bins
plt.ylabel("frequency")
plt.xlabel("CUI")

plt.savefig('hist.png')

