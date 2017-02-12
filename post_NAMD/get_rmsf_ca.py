# Usage:
#	python get_rmsf_ca.py $PSF $DCD $OUTPUT 
import sys
import numpy as np
import MDAnalysis as mda
import matplotlib.pyplot as plt
from matplotlib import rcParams

if len(sys.argv) != 4:
	print("Usage: python get_rmsf_ca.py $PSF $DCD $OUTPUT ")
	sys.exit(-1)

psf_file = sys.argv[1]
dcd_file = sys.argv[2]
out_file = sys.argv[3] + '.png'

u = mda.Universe(psf_file, dcd_file)

ca = u.select_atoms("name CA")
means = np.zeros((len(ca), 3))
sumsq = np.zeros_like(means)
for k, ts in enumerate(u.trajectory):
	sumsq += (k/(k+1.0)) * (ca.positions - means)**2
	means[:] = (k*means + ca.positions)/(k+1.0)
rmsf = np.sqrt(sumsq.sum(axis=1)/(k+1.0))

import seaborn.apionly as sns
#matplotlib inline
plt.style.use('ggplot')
rcParams.update({'figure.autolayout': True})
sns.set_style('ticks')
fig = plt.figure(figsize=(5,3))
ax = fig.add_subplot(111)
color = sns.color_palette()[2]
#ax.fill_between(ca.residues.resids, rmsf, alpha=0.3, color=color)
ax.plot(ca.residues.resids, rmsf, lw=1, color=color)
sns.despine(ax=ax)
ax.set_xlabel("Residue Number")
ax.set_ylabel(r"C$_\alpha$ RMSF ($\AA$)")
ax.set_xlim(min(ca.residues.resids), max(ca.residues.resids))
ax.set_ylim(0, 10)
fig.savefig(out_file)
