set psfname [lindex $argv 0]
set dcdname [lindex $argv 1]
set psf_suffix ".psf"
set output "_5ps_traj.pdb"
set output2 "_frame0.pdb"
mol new $psfname$psf_suffix
mol addfile $dcdname waitfor 20000
set ref [atomselect 0 "backbone" frame 0]
set sel [atomselect 0 "backbone"]
set all [atomselect 0 all]
set n [molinfo 0 get numframes]
for { set i 1 } { $i < $n } { incr i } {
	$sel frame $i
	$all frame $i
	$all move [measure fit $sel $ref]
}
$ref delete
$all delete
$sel delete

##Write out the first frame
#set frame0 [atomselect 0 all frame 0]
#$frame0 writepdb $psfname$output2

animate write pdb $psfname$output
