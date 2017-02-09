set molname [lindex $argv 0]
set pdbsuffix "_wb.pdb"
set psfsuffix "_wb.psf"
set outputsuffix "_wb_i"
package require autoionize
# Only neutralize the systen
# autoionize -psf $molname$psfsuffix -pdb $molname$pdbsuffix -neutralize -o $molname$outputsuffix

# Neutralize the system and set NaCl concentration as 0.15 mol/L
autoionize -psf $molname$psfsuffix -pdb $molname$pdbsuffix -sc 0.15 -cation POT -o $molname$outputsuffix
