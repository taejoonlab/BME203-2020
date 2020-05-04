Pfam SARS-CoV-2, special release 
--------------------------------

v1.0 02/04/2020
We have reviewed all of the Pfam entries that match against the proteins 
encoded by SARS-CoV-2, and added a few additional entries to provide as 
comprehensive set of annotations as possible. We have improved the naming 
consistency of these Pfam entires and updated the descriptions. As this is 
a special release of Pfam, these updates are not yet available on the 
Pfam website. We anticipate making them available in 6-8 weeks. 

The files currently available are:
1. Pfam-A.SARS-CoV-2.hmm  - this is the mini Pfam HMM library.
2. matches.scan - the matches to SARS-CoV-2 using hmmscan.
3. covid-19.fasta - the SARS-CoV-2 proteins from UniProt.

How to use this library?
------------------------
This library is not compatible with the pfam_scan software that we normally 
recommend to reproduce Pfam matches, as this library only contains a small 
subset of models.  If you wish to compare these models to your own sequences, 
please use the following HMMER commands:

$ hmmpress  Pfam-A.SARS-CoV-2.hmm

This only needs to be performed once. Then to compare your sequences (in a file 
called my.fasta) to this special Pfam profile HMM library, then:  

$ hmmscan --cut_ga --domtblout matches.scan Pfam-A.SARS-CoV-2.hmm my.fasta

The --domtblout option enables you to save the matches in a more convenient 
tabular form, if you do not want to parse the HMMER output.


