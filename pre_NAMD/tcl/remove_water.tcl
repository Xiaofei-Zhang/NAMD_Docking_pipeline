set molname [lindex $argv 0]
set pdbsuffix ".pdb"
set outputsuffix "_p.pdb"
mol new $molname$pdbsuffix
set patoms [atomselect top protein]
$patoms writepdb $molname$outputsuffix
