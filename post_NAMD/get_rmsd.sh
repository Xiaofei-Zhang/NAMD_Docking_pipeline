#!/bin/bash

python get_rmsd.py 1Y57_model_wb_i.psf 1Y57_model_wb_i.pdb 1Y57_model_wb_i_production10.dcd 1Y57_prod10_rmsd

python get_rmsf_ca.py 1Y57_model_wb_i.psf 1Y57_model_wb_i_production10.dcd 1Y57_prod10_ca_rmsf
