import random

Account_Dictionary={}
account_list=()
def acc_num_gen():
    global acc_num
    acc_num=str(random.randint(1000000,999999))
    if acc_num not in account_list:
        account_list.append(acc_num)
    else:
        acc_num()


def Re_Enter_Info():
    print('')


def New_user():
    Name=str(input('Enter the Your Name: '))
    input_Starting_bal=str(input('Enter the Starting Balance: '))
    Age=str(input('Enter the Your age: '))
    if Name.isalpha():
        if input_Starting_bal>=1000:
            if Age>=16:
                acc_num_gen()
                Account_Dictionary[acc_num]=[Name , input_Starting_bal , Age]
                print(Account_Dictionary[acc_num])


input_fil=0
while input_fil==0:
    enter_option=int(input('Enter your choice : \n 1. Register a New User \n 2. Deposit Money \n 3. Close/Delete Account \n 4. Display all accounts'))
    if enter_option==1 :
            New_user()
    else:
        print("")
        print("Admission number not valid please enter again")
        print("")

