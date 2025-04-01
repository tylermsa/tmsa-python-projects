#!/usr/bin/python
# -*- coding: ascii -*-

"""
    Powered by tylermsa
    Made back in late-2020/ early-2021 back when I used Python 2
    Updated in 2025 Thanks to Python3
"""# TODO: Look up how to add ASCII Characters on Linux os files

from random import *
# raw = raw.encode('ascii', 'ignore')

def draw_square(par1_dom, par1_res, par2_dom, par2_res):
	#Print seperate space
	print(" ")
	#Print Parent 1 Genes
	print("     {}  |  {}".format(par1_dom, par1_res))
	# raw = raw.encode('ascii', 'ignore')
	#Print Borders
	print("   ===========")	
	# raw = raw.encode('ascii', 'ignore')
	#Print Parent 2 gene1, border, and top punnet
	print(" {} | {}{} | {}{} |".format(par2_dom, par1_dom, par2_dom, par2_dom, par1_res))
	# raw = raw.encode('ascii', 'ignore')
	print(" - |----|----|")
	# raw = raw.encode('ascii', 'ignore')
	#Print Parent 2 gene1, border, and bottom punnet
	print(" {} | {}{} | {}{} |".format(par2_res, par1_dom, par2_res, par2_res, par1_res))
	# raw = raw.encode('ascii', 'ignore')
	print("   ===========")
	print(" ")
	
	
	# 
	#     E  |  x
	#   ===========
	# E | EE | Ex |
	# - |----|----|
	# x | Ex | xx |
	#   ===========


parent1 = " "
parent2 = " "

print("Python Punnett Square")
print("powered by tylermsa")
print("- - - - - - - - - - - - - - - - - - - - - - - -")
print(" ")

#print("Enter the gene pair of Parent 1:")
parent1 = input("Enter the gene pair of Parent 1: ") # replacing raw_input() since that has been deprecated in python3


#print("Enter the gene pair of Parent 2:")
parent2 = input("Enter the gene pair of Parent 2: ") # replacing raw_input() since that has been deprecated in python3

draw_square(parent1[:1], parent1[1:], parent2[:1], parent2[1:])


# End of Code
