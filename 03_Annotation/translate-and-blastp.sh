transeq --sequence ../data/GCF_009858895.2_ASM985889v3_genomic.fna --outseq ASM985889v3_trans6.fa -frame 6

makeblastdb -dbtype prot -in ASM985889v3_trans6.fa -out ASM985889v3_trans6

blastp -db ASM985889v3_trans6 -query ../data/GCF_009858895.2_ASM985889v3_protein.faa -outfmt 7 -out REF.ASM985889v3_trans6.tbl
