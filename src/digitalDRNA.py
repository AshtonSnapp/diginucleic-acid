###############################################################################
# 		Project: Binary format for storing DNA/RNA nucleotides, editor program.
#  Date Created: April 18, 2019
# Date Modified: April 18, 2019
################################################################################

#---===[ Necessary Imports ]===---#

import tkinter as gui

#---===[ Constant Definitions ]===---#

# Define binary integer constants. First bit differentiates between Purine / Pyrimidine, second bit chooses actual nucleotide.

ADENINE = 0b00
GUANINE = 0b01
THYMINE = 0b10  # Also represents Uracil, but just using the name for one of them is shorter
CYTOSINE = 0b11 # Had to mess up the alignment. Screw you, Cytosine

# Define codons that create certain amino acids. Default Codon Profile?

PHENYLALANINE = ["TTT", "TTC"]
LEUCINE = ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"]
ISOLEUCINE = ["ATT", "ATC", "ATA"]
METHIONINE = "ATG"
VALINE = ["GTT", "GTC". "GTA", "GTG"]
SERINE = ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"]
PROLINE = ["CCT", "CCC", "CCA", "CCG"]
THREONINE = ["ACT", "ACC", "ACA", "ACG"]
ALANINE = ["GCT", "GCC", "GCA", "GCG"]
TYROSINE = ["TAT", "TAC"]
STOP = ["TAA", "TAG", "TGA"]
HISTIDINE = ["CAT", "CAC"]
GLUTAMINE = ["CAA", "CAG"]
ASPARAGINE = ["AAT", "AAC"]
LYSINE = ["AAA", "AAG"]
ASPARTATE = ["GAT", "GAC"]
GLUTAMATE = ["GAA", "GAG"]
CYSTEINE = ["TGT", "TGC"]
TRYPTOPHAN = "TGG"
ARGININE = ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"]
GLYCINE = ["GGT", "GGC", "GGA", "GGG"]