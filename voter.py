choice='y'
while(choice=='y'):
    age=int(input("Enter your age...:"))
    if(age<18):
        print("You are underage and cannot vote!")
    elif(age==18):
        print("You are now 18 and can vote if you have a voter's ID card!")
    elif(age>18):
        print("You are an eligible voter who can vote his/her representative!")
    choice=input("Do you want to continue:(y/n)...:")
    if(choice=='y'):
        continue
    else:
        break