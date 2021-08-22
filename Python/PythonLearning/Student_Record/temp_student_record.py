


fd=open(r"./template_mine.txt","r")
header=fd.readlines()
header_format=header[0].split(",")
fd.close()

fd=open("./Student_mine.txt","r")
string=fd.readlines()
temp_header=string[0].split(",")
temp_header[3]=temp_header[3].strip()
len_std_record=len(string)
fd.close()

student=[]
for i in range(1,len_std_record):
    student.append(string[i][:-1].split(","))


temp_dict_list=[]
actual_dict_list=[]
marks_list=[]
std_names_list=[]
No_students=len(student)
file_names_list=[]
std_id_list=[]
for i in range(No_students):
    temp_dict_list.append(dict(zip(temp_header,student[i])))
    actual_dict_list.append({item:temp_dict_list[i][item] for item in header_format})
    file_names_list.append(actual_dict_list[i]["std_name"]+"."+actual_dict_list[i]["std_id"]+".txt")
    marks_list.append(actual_dict_list[i]["marks"])
    std_names_list.append(actual_dict_list[i]["std_name"])
    std_id_list.append(actual_dict_list[i]["std_id"])

n=len(actual_dict_list)

for i in range(n):
    for j in range(n):
        if i is not j :
            if actual_dict_list[i]["std_id"]==actual_dict_list[j]["std_id"]:                
                with open("%s"%file_names_list[i],"a+") as fo:
                          fo.seek(0,0)
                          if str(actual_dict_list[i]["subject"]) not in fo.read():                
                              fo.write(str(actual_dict_list[i]))
                              fo.write("\n")                              
                              fo.close()
            else:
                with open("%s"%file_names_list[j],"a+") as fo:
                          fo.seek(0,0)
                          if str(actual_dict_list[j]["subject"]) not in fo.read():                
                              fo.write(str(actual_dict_list[j]))
                              fo.write("\n")                              
                              fo.close()

'''
#######################################################
Calculating Total Marks of students in all the subjects
#######################################################
'''

for i in range(len(std_id_list)):
    for j in range(len(std_id_list)):
        if i is not j:
            if std_id_list[i]==std_id_list[j]:
                Total=int(marks_list[i])+int(marks_list[j])
                fo=open("%s.%d.txt"%(std_names_list[i],int(std_id_list[i])),"a+")
                fo.seek(0,0)
                if "Total" not in fo.read():
                    fo.write("Total:"+str(Total))
                    print("Total Marks of "+std_names_list[i]+" : "+str(Total))
                    fo.close()
            else:
                fo=open("%s.%d.txt"%(std_names_list[j],int(std_id_list[j])),"a+")
                fo.seek(0,0)
                if len(fo.readlines())==1:
                    Total=int(marks_list[j])
                    fo.write("Total:"+str(Total))
                    print("Total Marks of "+std_names_list[j]+" : "+str(Total))
                    fo.close()
                

