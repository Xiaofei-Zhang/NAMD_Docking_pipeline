# get_enrichment.py
# Creates the text file for the enrichment plot
#
# Usage:
#	python get_enrichment.py $INPUT $RECEPTOR $ACTIVE $DECOY
# 
# $INPUT=the sorted_results file of docking results
# $RECEPTOR=the name of receptor
# $ACTIVE=the label string of the active ligands
# $DECOY=the label string of the decoy ligands
#
# The sorted affinity file name will be $RECEPTOR_$ACTIVE_$DECOY_sorted.txt
# The enrichment file name will be $RECEPTOR_$ACTIVE_$DECOY_enrichment.txt
# 
# Authors: Xiaofei Zhang, Sally R. Ellingson
# Date: June 18 2016


from __future__ import print_function
import sys

# print_error: function to print out the error message
def print_error(*args, **kwargs):
	        print(*args, file=sys.stderr, **kwargs)

# get_sorted_records: function to sort the affinity data to file
def get_sorted_records(infile, receptor_name, active_name, decoy_name, records):
	for line in infile:
		if receptor_name in line and (decoy_name in line or active_name in line):
			split_line = line.split()
			energy = float(split_line[1])
			if energy not in records:
				records[energy] = []
			records[energy].append(split_line[2])
	sorted_records = sorted(records.keys())
	size_records = len(sorted_records)
	sorted_filename = receptor_name + "_" + active_name + "_" + decoy_name + "_sorted.txt"
	sorted_file = open(sorted_filename, 'w')
	rank = 1
	sorted_file.write('Rank\tEnergy\tLigand')
	for energy in sorted_records:
		num_ener=len(records[energy])
		for x in range(num_ener):
  			sorted_file.write('\n'+str(rank)+'\t'+str(energy)+'\t'+records[energy][x])
			rank = rank + 1
	sorted_file.close()

# get_enrichment: function to generate the enrichment file for plot
def get_enrichment(sorted_filename, receptor_name, active_name, decoy_name):
	sorted_file = open(sorted_filename, 'r')
	elist = []
	lcount = 0
	tcount = 0

	first = 1
	for line in sorted_file:
		if first == 0:
			split_line = line.split()
			lig_name = split_line[2]
			if active_name in lig_name:
				lcount = lcount+1
				elist.append(1)
				tcount = tcount + 1
			if decoy_name in lig_name:
				elist.append(0)
				tcount = tcount + 1
		else:
			first = 0
	sorted_file.close()
	enrichment_filename = receptor_name + "_" + active_name + "_" + decoy_name + "_enrichment.txt"
	enrichment_file = open(enrichment_filename, 'w')
	current_lcount = 0
	current_tcount = 0
	for e in elist:
		current_lcount = current_lcount + e
		current_tcount = current_tcount + 1

		percentl = float(current_lcount) / lcount * 100
		percentt = float(current_tcount) / tcount * 100
		enrichment_file.write(str(percentt) + '\t' + str(percentl) + '\n')
	enrichment_file.close()
	
		



# main
if len(sys.argv) != 5:
	print_error("Usage: python get_enrichment.py $INPUT $RECEPTOR $ACTIVE_LIGAND $DECOY_LIGAND")
	sys.exit(-1)

try:
	infile=open(sys.argv[1], 'r')
except (OSError, IOError) as e:
	print_error("Failed to open file: " + sys.argv[1])
	sys.exit(-1)

receptor_name = sys.argv[2]
active_name = sys.argv[3]
decoy_name = sys.argv[4]
records = {}
get_sorted_records(infile, receptor_name, active_name, decoy_name, records)
sorted_filename = receptor_name + "_" + active_name + "_" + decoy_name + "_sorted.txt"
get_enrichment(sorted_filename, receptor_name, active_name, decoy_name)
# main_end
