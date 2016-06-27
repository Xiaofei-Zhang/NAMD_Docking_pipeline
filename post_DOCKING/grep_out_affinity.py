##############################################################################################
#	Author: Sally R. Ellingson
#	Date: June 16, 2011
#	Use: Call script in directory of *.pdbqt files created by Autodock Vina
#	Results: unsorted list affinity energy
#	Output: Order	Energy	Ligand(from pdbqt file name)
##############################################################################################

import glob


#get list of result files in directory
file_list=glob.glob('*.pdb*')

#dict for storing results
results={}


print len(file_list)
out_file=open('mydocking_results', 'w')
rank=1
out_file.write('Order\tEnergy\tLigand')


for file_name in file_list:
  result_file=open(file_name, 'r')
  line=result_file.readline()
  #skip to best energy
  line=result_file.readline()
  #get energy
  energy_line=line.split()
  if len(energy_line) >= 4:
    best_energy=float(energy_line[3])
    out_file.write('\n'+str(rank) + '\t' + str(best_energy) + '\t'+ file_name)
    rank=rank+1
  result_file.close()


out_file.close()
