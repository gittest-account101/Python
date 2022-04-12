def ques1():
    def sum(x,y):
        x+=1
        y+=1
        return x , y
    a=2
    b=3
    print(a , b , "\n")
    a,b=sum(a,b)
    print(a ,b)

def ques2():
    #hello
    x={1:'a', 2:"b" , 3:{31:"ba" , 32:'bb' ,33:{331:'bba'}}}
    print(x[3][33][331])

ques2()