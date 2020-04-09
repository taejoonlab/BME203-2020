#!/usr/bin/env python
# coding: utf-8

# In[2]:


def read_fasta(tmp_filename):
    rv = dict()
    f = open(tmp_filename, 'r')
    for line in f:
        if line.startswith('>'):
            tmp_h = line.strip().lstrip('>')
            rv[tmp_h] = ''
        else:
            rv[tmp_h] += line.strip().replace(' ', '')
    f.close()
    return rv


# In[4]:


filename_genomes = '2019nCoV_genomes.2020_03_27.fa'
genome_list = read_fasta(filename_genomes)
print('The number of sequences in the genome are ' + str(len(genome_list)))
print('The lengths of the sequences are as follow')
for g_h, g_seq in genome_list.items():
    print(g_h.split()[0], g_seq[:20],'     The length of the sequence is ' + str(len(g_seq)))
    
for x1,x2 in genome_list.items():
    for y1,y2 in genome_list.items():
        if x2==y2 and y1 != x1 and y1>x1:
            print(x1.split()[0] ,'and', y1.split()[0], 'are identical')


# In[ ]:





# In[ ]:




