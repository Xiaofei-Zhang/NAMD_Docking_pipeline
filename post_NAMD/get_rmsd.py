# Usage:
#	python get_rmsf_ca.py $PSF $PDB $DCD $OUTPUT 
import sys
import numpy as np
import MDAnalysis as mda
import MDAnalysis.analysis.rms
import matplotlib.pyplot as plt
from matplotlib import rcParams

if len(sys.argv) != 5:
	print("Usage: python get_rmsd.py $PSF $PDB $DCD $OUTPUT ")
	sys.exit(-1)

psf_file = sys.argv[1]
pdb_file = sys.argv[2]
dcd_file = sys.argv[3]
dat_file = sys.argv[4] + '.dat'
out_file = sys.argv[4] + '.png'

u = mda.Universe(psf_file, dcd_file)
ref = mda.Universe(psf_file, pdb_file) # default the 0th frame

R = MDAnalysis.analysis.rms.RMSD(u, ref, select = "backbone", filename=dat_file)

R.run()
R.save()

rmsd = R.rmsd.T
time = rmsd[1]
import seaborn.apionly as sns
#matplotlib inline
plt.style.use('ggplot')
rcParams.update({'figure.autolayout': True})
sns.set_style('ticks')
fig = plt.figure(figsize=(5,3))
ax = fig.add_subplot(111)
color = sns.color_palette()[2]
#ax.fill_between(ca.residues.resids, rmsf, alpha=0.3, color=color)
ax.plot(time, rmsd[2], lw=1, color=color)
sns.despine(ax=ax)
ax.set_xlabel("Time (ps)")
ax.set_ylabel(r"RMSD ($\AA$)")
ax.set_xlim(0, max(time))
ax.set_ylim(0, 10)
fig.savefig(out_file)
