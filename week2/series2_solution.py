#--------------#
# Question 3.1 #
#--------------#

from Bio import SeqIO
genome = SeqIO.read("chrI.fa", "fasta")  # This creates a 'SeqRecord' object

"""
Alternatively:

f = open("chrI.fa")
genome = f.read()
f.close()

Note that in this case all the file is read as a single string.
For large genomes this could cause memory problems! It is even worse with annotation files.
Note also the multiple-line comment we use here.
"""

#--------------#
# Question 3.2 #
#--------------#

total_length = len(genome.seq)  # genome.seq is a 'Seq' object, similar to a string
print "The length is:", total_length

"""
Alternatively:

total_length = len(genome)
print "The length is:", total_length
"""

#--------------#
# Question 3.3 #
#--------------#

A_count = genome.seq.count('A') + genome.seq.count('a')
C_count = genome.seq.count('C') + genome.seq.count('c')
G_count = genome.seq.count('G') + genome.seq.count('g')
T_count = genome.seq.count('T') + genome.seq.count('t')
print 'A: %s, C: %s, G: %s, T: %s' % (A_count, C_count, G_count, T_count)
# each '%s' will be replaced by the corresponding string on the right of the '%'

"""
Alternatively:
a=0; c=0; g=0; t=0; n=0
for base in genome:
    base = base.lower() # lower() transforms characters to lower case
    if base == 'a': a+=1 # equivalent to a = a+1
    elif base == 'c': c+=1
    elif base == 'g': g+=1
    elif base == 't': t+=1
    else: n+=1 # There are 'N's in the file to indicate repeated (uninteresting) sequences.
"""

#--------------#
# Question 3.4 #
#--------------#

from Bio.SeqUtils import GC
gc_percentage = GC(genome.seq)
print "The total GC percentage is:", gc_percentage

#---------------------------#
# Question 3.5(a) computing #
#---------------------------#

number_of_windows = 1000 # Arbitrary
window_size = total_length / number_of_windows
start_positions = range(0, total_length, window_size)
gc_per_window = []

for start in start_positions:
    stop  = start + window_size
    gc_in_window = GC(genome[start:stop].seq)
    gc_per_window.append(gc_in_window)

#--------------------------#
# Question 3.5(b) plotting #
#--------------------------#

from matplotlib.pyplot import *
plot(start_positions, gc_per_window)
title("GC content with a window size of %i base pairs" % window_size)
xlabel("Genome position [base pairs]")
ylabel("GC content [%]")
show()

#--------------#
# Question 3.6 #
#--------------#

f = open('gc_per_window.txt', 'w')
for i in range(number_of_windows):
    start = start_positions[i]
    stop  = start_positions[i] + window_size
    gc    = gc_per_window[i]
    line  = "%i\t%i\t%f\n" % (start, stop, gc) # %i - integer, %f - float, "\t" - tab, "\n" - newline
    f.write(line)
f.close()
