#!/bin/bash
#SBATCH -p Long
#SBATCH -N 1
#SBATCH --mail-type=ALL

$VMD -dispdev text -eofexit < /home/xzh289/Scripts/MD_Analysis/align.tcl -args 1QCF_p 1QCF_100ns.dcd
