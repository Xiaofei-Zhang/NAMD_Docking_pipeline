#!/bin/bash

$CATDCD -o 1QCF_100ns_10ps.dcd -first 1 -last 200000 -stride 20 1QCF_100ns.dcd
$CATDCD -o 1QCF_100ns_2ps.dcd -first 1 -last 200000 -stride 4 1QCF_100ns.dcd
$CATDCD -o 1QCF_100ns_20ps.dcd -first 1 -last 200000 -stride 40 1QCF_100ns.dcd
