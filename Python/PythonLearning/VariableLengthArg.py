def printinfo( arg1, *vartuple ):
   "This prints a variable passed as arguments"
   print("Output is:")
   print(arg1)
   print(vartuple)
   #for var in vartuple:
    #  print(var)
   #return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
