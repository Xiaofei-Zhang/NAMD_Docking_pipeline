#!/bin/bash
sed '/CRYST/d' 1QCF_p_traj.pdb > 1QCF_traj.pdb
sed -i -e 's/END/ENDMDL/g' 1QCF_traj.pdb
