set molname [lindex $argv 0]
set pdbsuffix ".pdb"
set outputpdb "_h.pdb"
set outputpsf "_h.psf"
mol new $molname$pdbsuffix
package require psfgen
topology /Users/Xiaofei/Documents/github/NAMD_Docking_pipeline/pre_NAMD/toppar/top_all27_prot_na.inp
pdbalias residue Y2P TYR
pdbalias residue HIS HSE
pdbalias residue HID HSD
pdbalias atom ILE CD1 CD
segment U {pdb $molname$pdbsuffix}
patch TP2 U:505
coordpdb $molname$pdbsuffix U
guesscoord
writepdb $molname$outputpdb
writepsf $molname$outputpsf
