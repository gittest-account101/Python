import random
x=1
while x<=20:
    r=['b' , 'a' ,'d' , 'c' , 'e' , 'h' , 'f']
    s= random.randint(1,3)
    e=random.randint(2,4)
    for k in range(s,e+1):
        print(r[k], end =' @ ')
    x+=1