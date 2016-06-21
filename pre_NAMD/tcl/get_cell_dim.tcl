puts "The list of arguments: $argv"
mol new [lindex $argv 0]
set sel [atomselect top all]
set c [measure center $sel] ;foreach {cx cy cz} $c {}
set m [measure minmax $sel] ;foreach {j1 j2} $m {} ;foreach {x2 y2 z2} $j2 {} ;foreach {x1 y1 z1} $j1 {}
set x [expr $x2 - $x1]
set y [expr $y2 - $y1]
set z [expr $z2 - $z1]
puts [open receptors.txt a] "[lindex $argv 1] [format "%.3f" $x] [format "%.3f" $y] [format "%.3f" $z] [format "%.3f" $cx] [format "%.3f" $cy] [format "%.3f" $cz]"

