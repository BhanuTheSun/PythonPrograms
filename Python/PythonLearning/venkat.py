
students = open("C:\PythonLearning\Student_Record\Student_mine.txt")
student_marks = {}
temporary_dict = {}
first = 1
template = open(r"C:\PythonLearning\Student_Record\template.txt").read()
#print(template)
output_format = [item.split(':')[0].strip() for item in template[1:-1].split(',')]
#print(output_format)
for item in students.readlines():
    #print(item)
    if first:
        headings = item[:-1].split(',')
        first = 0
        continue
    #print(headings)
    student_data = item[:-1].split(',')
    #print(student_data)   
    temporary_dict = {headings[index]:item for index,item in enumerate(student_data)}
    #print(temporary_dict)
    student_name_id = temporary_dict["std_name"]+"."+temporary_dict["std_id"]+".txt"
    #print(student_name_id)
    if student_name_id not in student_marks:
        student_marks[student_name_id] = int(temporary_dict["marks"])        
    else:
        student_marks[student_name_id]+=int(temporary_dict["marks"])
        f = open(student_name_id,"a+")
        f.write('{')
        temporary_list = [[item,temporary_dict[item]] for item in output_format]
        l,j=len(temporary_list),0

        for i in temporary_list:

            if(j!=l-1):
                s=","
            else:
                s=""
            f.write(str(i[0])+":"+str(i[1])+s)
            j=j+1
        f.write('}\n')

        f.close()
    print(student_marks)
    for key in student_marks:
        open(key,"a+").write("Total:"+str(student_marks[key]))

