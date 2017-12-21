#!/usr/bin/python

import sys


oper = sys.argv[1]

if oper=='add':
	print (int(sys.argv[2])+int(sys.argv[3]))
elif oper=='subtract':
	print (int(sys.argv[2])-int(sys.argv[3]))
elif oper=='multiply':
	print (int(sys.argv[2])*int(sys.argv[3]))
elif oper=='divide':
	print (int(sys.argv[2])/int(sys.argv[3]))
