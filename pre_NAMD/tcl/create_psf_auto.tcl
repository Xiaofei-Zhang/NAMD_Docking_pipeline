set molname [lindex $argv 0]
set pdbsuffix "_p.pdb"
set outputprefix "_p_h"
mol new $molname$pdbsuffix
package require autopsf
autopsf -mol 0 -prefix $molname$outputprefix
