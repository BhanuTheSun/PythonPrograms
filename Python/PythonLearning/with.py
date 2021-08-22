with open("C:\PythonLearning\Student_Record\Student.txt") as f:
    if 'Bhanu' in f.read():
        print("true")
    else:
        print("False")
