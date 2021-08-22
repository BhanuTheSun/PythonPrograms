#!/usr/bin/python

import os

os.rmdir("C:\PythonLearning\Phone")
os.mkdir("C:\PythonLearning\Phone")
os.chdir("C:\PythonLearning\Phone")

fd=open("__init__.py","w+")
fd.close()
fd=open("Pots.py","w+")
fd.close()
fd=open("Isdn.py","w+")
fd.close()
fd=open("G3.py","w+")
fd.close()
