# get_AUC.py: Calculate and print out the AUC of the enrichment data
# Usage:
#	python get_AUC.py $ENRICHMENT
#
# $ENRICHMENT is the enrichment file contains the enrichmet data

import sys

infile=open(sys.argv[1], 'r')
x=[]
y=[]
for line in infile:
	split_line=line.split()
	a = float(split_line[0])
	b = float(split_line[1])
	x.append(a)
	y.append(b)

currentp = 0
auc = 0
rangeX = len(x)-1
added = 0
for i in range (rangeX):
	currentp = y[i]*(x[i+1]-x[i])
	added = (y[i+1] - y[i])*(x[i+1]-x[i])
	auc = auc + currentp + added
print ("AUC: "+str(auc))
