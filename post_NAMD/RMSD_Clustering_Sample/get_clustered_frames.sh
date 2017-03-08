#!/bin/bash

#SBATCH -p Long
#SBATCH -n 16
#SBATCH --mail-type=ALL

sed -n 28373,35464p ../1Y57_5ps_traj.pdb > 1Y57_frame4.pdb
sed -n 131326896,131333987p ../1Y57_5ps_traj.pdb > 1Y57_frame18515.pdb
sed -n 9412412,9419503p ../1Y57_5ps_traj.pdb > 1Y57_frame1327.pdb
sed -n 44047531,44054622p ../1Y57_5ps_traj.pdb > 1Y57_frame6210.pdb
sed -n 34713143,34720234p ../1Y57_5ps_traj.pdb > 1Y57_frame4894.pdb
sed -n 83101589,83108680p ../1Y57_5ps_traj.pdb > 1Y57_frame11716.pdb
sed -n 54289823,54296914p ../1Y57_5ps_traj.pdb > 1Y57_frame7654.pdb
