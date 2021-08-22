fd_tmp=open(r"C:\PythonLearning\Student_Record\template_mine.txt","r+")
header=fd_tmp.readlines()
header_list=header[0].split(",")
#print(header_list)

fd_tmp.close()

fd=open("C:\PythonLearning\Student_Record\Student_mine.txt","r")
string=fd.readlines()
len_stud_record=len(string)
fd.close()

student=[]
for i in range(1,len_stud_record):
    student.append(string[i].split(","))

#print(student)


student_info=[]
No_students=len(student)
for i in range(No_students):
    student_info.append(dict(zip(header_list,student[i])))

print(student_info)

n=len(student_info)
#print(n)
for i in range(n):
    for j in range(n):
        if i is not j :
            if student_info[i]["std_id"]==student_info[j]["std_id"]:                
                with open("%s.%d.txt"%(student_info[i]["std_name"],int(student_info[i]["std_id"])),"a+") as fo:
                          fo.seek(0,0)
                          if str(student_info[i]["marks"]) not in fo.read():                
                              fo.write(str(student_info[i]))
                              fo.write("\n")
                              fo.close()                              
            else:
                with open("%s.%d.txt"%(student_info[j]["std_name"],int(student_info[j]["std_id"])),"a+") as fo:
                          fo.seek(0,0)
                          if str(student_info[j]["marks"]) not in fo.read():                
                              fo.write(str(student_info[j]))
                              fo.write("\n")
                              fo.close()
    
    


    
'''

first=dict(zip(header_list,student[0]))
second=dict(zip(header_list,student[1]))
Third=dict(zip(header_list,student[2]))

print(first)
print(second)
print(Third)
first=dict(zip(header_list,first_student))
second=dict(zip(header_list,second_student))
Third=dict(zip(header_list,Third_student))


list_dictionary.append(first)
list_dictionary.append(second)
list_dictionary.append(Third)

print(list_dictionary)
n=len(list_dictionary)
print(n)
for i in range(n):
    for j in range(n):
        if n<3:
            if(list_dictionary[i]["std_id"]==list_dictionary[j]["std_id"]):
                print("Name of the student with same std_id",list_dictionary[i]["std_name"])
    
    
    
    
#search_ele=first["std_id"]
#print(search_ele)


#print(list_dictionary)
#if search_ele in Third["std_id"]:
 #   print("first and Third are related to",first["std_name"])
  #  fd=open("C:\PythonLearning\first[std_name].first[std_id].txt","w+")

#print(first)
#print(second)
#print(Third)



#student_list=string.split(",")
#print(student_list)

'''
