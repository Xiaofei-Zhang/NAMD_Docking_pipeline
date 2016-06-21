# prepare_receptors.py
# Create the .pdbqt files and receptors coordinates file of receptors
# for VinaMPI Docking
# Usage:
#	python prepare_receptors.py
#
# Specify the correct paths of prepare_receptor4.py pythonsh VMD
# Make sure the get_AS_grid.tcl file uses the correct residue number
# of the active sites
# Run the scripts in the folder contains all receptors .pdb file
#
# Output: .pdbqt file for each .pdb
#	receptors.txt: used in VinaMPI
#
# Authors: Xiaofei Zhang, Sally R. Ellingson
# Date: June 21 2016



import os, glob, sys, shlex, subprocess

mypath = os.path.realpath(__file__)
tclpath = os.path.split(mypath)[0] + os.path.sep + 'tcl' + os.path.sep

# Set the path of prepare_receptor4.py
prepReceptor='/Users/Xiaofei/Documents/2016SpringRA/mgltools_i86Darwin9_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py'

# Set the path of pythonsh
pythonsh='/Users/Xiaofei/Documents/2016SpringRA/mgltools_i86Darwin9_1.5.6/bin/pythonsh'

# Set the path of VMD
vmd='/Volumes/VMD-1.9.2/VMD 1.9.2.app/Contents/vmd/vmd_MACOSXX86'

receptor_list=glob.glob('*.pdb')

# Create pdbqt files
for pdbfile in receptor_list:
	pdbqtfile = pdbfile[:-3]+'pdbqt'
	os.system(pythonsh + ' ' + prepReceptor + ' -r ' + pdbfile + ' -o ' + pdbqtfile +' -A hydrogens')

# Create receptors.txt file
with open('receptors.txt','w') as f:
	f.write('receptor size_x size_y size_z center_x center_y center_z cpu=1\n')
for pdbfile in receptor_list:
	pdbid = pdbfile[:-4]
	os.system('\"'+ vmd + '\"' +' -dispdev text -eofexit < '+ tclpath + 'get_AS_grid.tcl' + ' ' + '-args' + ' '+ pdbid)





