set molname [lindex $argv 0]
set pdbsuffix "_p.pdb"
set outputpdb "_p_h.pdb"
set outputpsf "_p_h.psf"
mol new $molname$pdbsuffix
package require psfgen
topology /Users/Xiaofei/Documents/2016SpringRA/Scripts/INP/top_all27_prot_lipid.inp
pdbalias residue HIS HSE
pdbalias atom ILE CD1 CD
segment U {pdb $molname$pdbsuffix}
coordpdb $molname$pdbsuffix U
guesscoord
writepdb $molname$outputpdb
writepsf $molname$outputpsf
