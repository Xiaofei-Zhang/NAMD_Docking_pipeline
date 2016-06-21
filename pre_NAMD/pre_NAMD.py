# pre_NAMD.py
# Creates the files used for NAMD based on the .pdb file dowloaded from PDB bank
# 
# Usage:
#	python pre_NAMD.py $PDBID
#
# $PDBID=the 4 characters identification code of the .pdb file
#
# Input: 
#    $PDBID.pdb: .pdb file downloaded from PDB bank
#
# Output:
#    $PDBID_p.pdb: .pdb file with water molecules removed
#    $PDBID_p_h.pdb: .pdb file with water removed and hydrogen atoms added
#    $PDBID_p_h.psf: .psf file of $PDBID_p_h.pdb
#    $PDBID_p_h.log: Log file of adding hydrogen atoms
#    $PDBID_wb.pdb: .pdb file of the water box model
#    $PDBID_wb.psf: .psf file of $PDBID_wb.pdb
#    $PDBID_wb.log: Log file of the water box model generation
#    $PDBID_wb_i.pdb: .pdb file of the ionized water box model (For NAMD)
#    $PDBID_wb_i.psf: .psf file of PDBID_wb_i.pdb (For NAMD)
#    $PDBID.log: Log file of the whole process (output of VMD)
#    $PDBID_center.txt: File contains the grid and center information of 
#       the ionized water box model
#
# Author: Xiaofei Zhang
# Date: June 20 2016

from __future__ import print_function
import sys, os

def print_error(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)


# main
if len(sys.argv) != 2:
        print_error("Usage: python pre_NAMD.py $PDBID")
	sys.exit(-1)

mypath = os.path.realpath(__file__)
tclpath = os.path.split(mypath)[0] + os.path.sep + 'tcl' + os.path.sep
pdbid = sys.argv[1]
logfile = pdbid+'.log'
# Using the right path of VMD
vmd = "/Volumes/VMD-1.9.2/VMD 1.9.2.app/Contents/vmd/vmd_MACOSXX86"

print("Input: "+pdbid+".pdb")
# Remove water
print("Remove water..")
cmdline = '\"'+ vmd + '\"' +' -dispdev text -eofexit < '+ tclpath + 'remove_water.tcl' + ' ' + '-args' + ' '+ pdbid +'> '+ logfile
os.system(cmdline)

# Create .psf
print("Create PSF file...")
cmdline = '\"'+ vmd + '\"' +' -dispdev text -eofexit < '+ tclpath + 'create_psf.tcl' + ' ' + '-args' + ' '+ pdbid +'>> '+ logfile
os.system(cmdline)

# Build water box
print("Build water box...")
cmdline = '\"'+ vmd + '\"' +' -dispdev text -eofexit < '+ tclpath + 'build_water_box.tcl' + ' ' + '-args' + ' '+ pdbid +'>> '+ logfile
os.system(cmdline)

# Add ions
print("Add ions...")
cmdline = '\"'+ vmd + '\"' +' -dispdev text -eofexit < '+ tclpath + 'add_ion.tcl' + ' ' + '-args' + ' '+ pdbid +'>> '+ logfile
os.system(cmdline)

# Calculate grid and center
print("Calculate center coordinates...")
cmdline = '\"'+ vmd + '\"' +' -dispdev text -eofexit < '+ tclpath + 'get_center.tcl' + ' ' + '-args' + ' '+ pdbid +'>> '+ logfile
os.system(cmdline)
print("Finish!")
# end main


