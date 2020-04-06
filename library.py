from Bio import pairwise2
from Bio.pairwise2 import format_alignment
X = "ATGTAGATCTGTTATTAAAGGTTTTAAAATCTGTGTGGCTGTCACTCCTC"
Y = "TTGTAGATCTGTTATTAAAGGTTTTAAAATCTGTGTGGCTGTCACTCCTC"

# Get a list of the global alignments between the two sequences ACGGGT and ACG satisfying the given scoring
# A match score is the score of identical chars, else mismatch score.
# Same open and extend gap penalties for both sequences.
alignments = pairwise2.align.globalms(X, Y,20, 0, 0, 0)



for a in alignments:
    print(format_alignment(*a))
