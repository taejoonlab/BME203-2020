#!/bin/bash

HMM="./Pfam_SARS-CoV-2_1.0/Pfam-A.SARS-CoV-2.hmm"
FA="GCF_009858895.2_ASM985889v3_protein.faa"

OUT=${FA/.fa/}".hmm_tbl"
LOG=$OUT".log"
echo $OUT

hmmscan --cut_ga --domtblout $OUT $HMM $FA >$LOG
