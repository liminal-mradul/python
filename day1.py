#!/usr/bin/env python
import sys, math  
r = float(sys.argv[1]) #extract the 1st command-line argument
s = math.sin(r)
print("hello, world!, sin(" + str(r) + ")=" + str(s))
