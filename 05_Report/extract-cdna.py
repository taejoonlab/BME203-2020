#!/usr/bin/env python3
import sys

query_id = 'RdRp|PRO_0000449629|P0DTD1'

query_list = dict()
f_in = open('../data/P0DTD1_chain.fa', 'r')
for line in f_in:
    if line.startswith('>'):
        tmp_h = line.strip().lstrip('>')
        query_list[tmp_h] = []
    else:
        query_list[tmp_h].append(line.strip())
f_in.close()

seq_list = dict()
f_fa = open('../data/2019nCoV_genomes.2020_04_14.fa', 'r')
for line in f_fa:
    if line.startswith('>'):
        tmp_h = line.strip().lstrip('>').split()[0]
        seq_list[tmp_h] = []
    else:
        seq_list[tmp_h].append(line.strip())
f_fa.close()

#print(">%s\n%s" % (query_id, ''.join(query_list[query_id])))

f_tbl = open('../data/P0DTD1_chain.2019nCoV_genomes.2020_04_14.tblastn_tbl', 'r')
for line in f_tbl:
    tokens = line.strip().split("\t")
    q_id = tokens[0]
    t_id = tokens[1]
    q_start = int(tokens[6])
    q_end = int(tokens[7])
    t_start = int(tokens[8])
    t_end = int(tokens[9])
    if q_id == query_id:
        q_len = len(''.join(query_list[q_id]))

        # print(q_start, q_end, t_start, t_end, q_len)
        t_start = t_start - (q_start-1) * 3
        t_end = t_start + q_len * 3
        # print(t_start, t_end, t_end - t_start)
        
        tmp_t_seq = ''.join(seq_list[t_id])
        tmp_t_fragment = tmp_t_seq[t_start-1:t_end]

        tmp_h = '%s-RdRp %s' % (t_id, query_id)
        print(">%s\n%s" % (tmp_h, tmp_t_fragment))
f_tbl.close()


