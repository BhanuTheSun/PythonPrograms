#!/usr/bin/python

fd=open("C:\PythonLearning\Test.txt","w+")
fd.write("BhanuChander is learning File I/O\n")
fd.close()

fd=open("C:\PythonLearning\Test.txt","r+")
string=fd.read()
print(string)
fd.close()

fd=open("C:\PythonLearning\Test.txt","a+")
fd.write("Appending text to existing file")
fd.close()

fd=open("C:\PythonLearning\Test.txt","r+")
string1=fd.read(12)
print(fd.tell())

for char in string1:
    print(char,end="")
fd.close()

