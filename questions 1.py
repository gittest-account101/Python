dict1 =dict()
i=1
num_students =int(input('Enter number of students: '))
print("")
while i<=num_students:
    adm=int(input('Enter the Admission Number: '))
    Name=str(input('Enter the Student Name: '))
    stu_class=str(input('Enter the Class: '))
    marks=str(input('Enter the Student marks: '))
    x=(Name, stu_class , marks)
    i+=1
    dict1[adm]=x
    print("\n")
y=dict1.keys()
list1=dict1.keys()


input_fil=0
while input_fil==0:
    enter_name=int(input('Enter the Admission No. for registered user : '))
    if enter_name in list1:
            print("")
            print("Admission Number", enter_name , ": ")
            print("Name\t" , "Class\t" , "Marks\t")
            for p in dict1[enter_name]:
                print(p, end="\t")
            print("")
            print('')
    else:
        print("")
        print("Admission number not valid please enter again")
        print("")