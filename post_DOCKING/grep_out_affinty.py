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

for file_name in file_list:
  result_file=open(file_name, 'r')
  line=result_file.readline()
  #skip to best energy
  line=result_file.readline()
  #get energy
  energy_line=line.split()
  if len(energy_line) >= 4:
    best_energy=float(energy_line[3])
 
  #store in dictionary
  if best_energy not in results:
    results[best_energy]=[]
  results[best_energy].append(file_name)
  result_file.close()

#print output
out_file=open('docking_results', 'w')
rank=1
out_file.write('Order\tEnergy\tLigand')
for energy in results:
  num_ener=len(results[energy])
  for x in range(num_ener):
    out_file.write('\n'+str(rank) + '\t' + str(energy) + '\t'+results[energy][x])
    rank=rank+1

out_file.close()
