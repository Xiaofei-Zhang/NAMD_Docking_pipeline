set molname [lindex $argv 0]
set inputsuffix ".pdb"
set output "receptors.txt"
mol new $molname$inputsuffix

# Modify the residue number of active sites for different PDB 
set sel [atomselect 0 "resid 253 259 271 273 288 314 316 to 320 322 371"]
set c [measure center $sel] ;foreach {cx cy cz} $c {}
set m [measure minmax $sel] ;foreach {j1 j2} $m {} ;foreach {x2 y2 z2} $j2 {} ;foreach {x1 y1 z1} $j1 {}
set x [expr $x2 - $x1]
set y [expr $y2 - $y1]
set z [expr $z2 - $z1]
puts [open $output a] "$molname [format "%.3f" $x] [format "%.3f" $y] [format "%.3f" $z] [format "%.3f" $cx] [format "%.3f" $cy] [format "%.3f" $cz]"
