from Bio import SeqIO
reads=list(SeqIO.parse("/share/data/class/genomes/Ecoli-genome/MG1655-K12.fasta","fasta"))
print len(reads)
print reads[0].seq[1379:1479].translate()

