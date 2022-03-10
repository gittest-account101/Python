def ques1():
    dict1={0:1 , 1:2 , 2:3 , 3:4 ,4:33}
    dict2={}
    x=len(dict1)
    y=1
    z=dict1.values()

    for i in z:
        if i%2!=0:
            zz=i*2
            dict2[y]=zz
            y+=1

    print(dict2)


def ques2():
    list1=[2,5,6,7,9,0]
    list2=[]
    list3=[]
    x=len(list1)
    y=x/2
    x=0
    xy=-1
    xx=0
    while xx!=y:
        list2.append(list1[xx])
        xx+=1
        list3.append(list1[xy])
        xy-=1

    list3.append(list2)
    print(list3)

def ques3():
    list1=[]
    list2=[]
    list3=[]
    n=int(input('Enter number of Numbers you want to enter: '))
    while (n>=1):
        name= str(input('Enter The Number: '))
        list1.append(name)
        n=n-1
    print('')
    print("The Original List" , list1)
    print('')
    x=int((len(list1))/2)
    list2.append(list1[:x])
    list3.append(list1[x:])
    list3.append(list2)
    print("The Changed List", list3)

def ques4():
    list1=[]
    n=int(input('Enter number of Numbers you want to enter: '))
    while (n>=1):
        name= str(input('Enter The Number: '))
        list1.append(name)
        n=n-1
    print('')
    print("The Original List" , list1)
    print('')
    x=int((len(list1))/2)
    y=list1[:x]
    for i in y:
        list1.remove(i)
    list1.append(y)
    print("The Changed List", list1)

ques4()
