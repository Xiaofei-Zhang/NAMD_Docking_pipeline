#!/bin/bash

#SBATCH -n 16
#SBATCH --mail-type=ALL


$GCLUSTER -n ../1QCF_selections.ndx -cutoff 0.175 -f ../1QCF_traj.pdb -s ../1QCF_fftraj.pdb -method gromos  -o -g -dist -ev -sz -ntr -clid -cl < 1.txt
