#!/usr/local/bin/python

import sys, os, shlex, subprocess

def main():
#	if len(sys.argv) != 3:
#		print("Usage: ./produce_enrichments.py $RESULT $CLUSTER $ACTV $DCY ")
#		sys.exit(-1)
	cmd1='grep \'CHEM\' 1QCF_docking_results > 1QCF_ACTIVE.txt'
	cmd2='grep \'ZINC\' 1QCF_docking_results > 1QCF_DECOY.txt'
	os.system(cmd1)
	os.system(cmd2)

	for i in range(1,8):
		cmd3 = 'grep \'cluster'+str(i)+'\' 1QCF_ACTIVE.txt > 1QCF_cluster' +str(i)+'.txt'
		cmd4 = 'grep \'cluster'+str(i)+'\' 1QCF_DECOY.txt >> 1QCF_cluster' +str(i)+'.txt'
		os.system(cmd3)
		os.system(cmd4)
		cmd5 = 'python $MD/post_DOCKING/get_enrichment.py 1QCF_cluster' +str(i)+'.txt 1QCF_cluster' +str(i)+ ' CHEM ZINC' 
		os.system(cmd5)
		cmd6 = 'python $MD/post_DOCKING/get_AUC.py 1QCF_cluster' + str(i)+'_CHEM_ZINC_enrichment.txt'
		os.system(cmd6)
# Main
if __name__ == '__main__':
    main()
