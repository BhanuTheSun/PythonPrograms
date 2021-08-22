fd_tmp=open(r"C:\PythonLearning\Student_Record\template_mine.txt","r+")
header=fd_tmp.readlines()
header_format=header[0].split(",")
fd_tmp.close()

fd=open("C:\PythonLearning\Student_Record\Student_mine.txt","r")
string=fd.readlines()
temp_header=string[0].split(",")
temp_header[3]=temp_header[3].strip()
print(temp_header)
len_stud_record=len(string)
fd.close()

student=[]
for i in range(1,len_stud_record):
    student.append(string[i][:-1].split(","))

print(student)
#print(student[0][0])


temp_dict_list=[]
actual_dict_list=[]
No_students=len(student)
for i in range(No_students):
    temp_dict_list.append(dict(zip(temp_header,student[i])))
    actual_dict_list.append({item:temp_dict_list[i][item] for item in header_format})

print(actual_dict_list)
#print(header_format)
#print(type(header_format))


#actual_dict = {item:student_info[i][item] for item in header_format}
#print(actual_dict)

#print(student_info)

n=len(actual_dict_list)
#print(n)
for i in range(n):
    for j in range(n):
        if i is not j :
            if actual_dict_list[i]["std_id"]==actual_dict_list[j]["std_id"]:               
                with open("%s.%d.txt"%(actual_dict_list[i]["std_name"],int(actual_dict_list[i]["std_id"])),"a+") as fo:
                          fo.seek(0,0)
                          if str(actual_dict_list[i]["subject"]) not in fo.read():                
                              fo.write(str(actual_dict_list[i]))
                              fo.write("\n")
                              fo.close()
            else:
                with open("%s.%d.txt"%(actual_dict_list[j]["std_name"],int(actual_dict_list[j]["std_id"])),"a+") as fo:
                          fo.seek(0,0)
                          if str(actual_dict_list[j]["subject"]) not in fo.read():                
                              fo.write(str(actual_dict_list[j]))
                              fo.write("\n")                              
                              fo.close()





