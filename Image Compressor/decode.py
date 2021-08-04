#coding: utf-8
from huffman_tree import *
 
coding_table = {'93': '1', '115': '0'}
 
file=input("Please box into the file name decoded by Huffman:")
f = open(file,'r')#, encoding='UTF-8'///'rb'
coding_result = f.readlines()[0].strip('\n')
width=int (input( "Please enter the width of the picture to be restored:"))
height = int(input("Please enter the height of the picture to be restored:"))
Decoding(width,height,coding_table,coding_result)