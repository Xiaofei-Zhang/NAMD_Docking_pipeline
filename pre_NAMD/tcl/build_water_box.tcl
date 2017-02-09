set molname [lindex $argv 0]
set pdbsuffix "_p_h.pdb"
set psfsuffix "_p_h.psf"
set outputsuffix "_wb"
package require solvate
solvate $molname$psfsuffix $molname$pdbsuffix -t 20 -o $molname$outputsuffix
