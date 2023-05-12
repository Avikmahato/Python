stack=[]

def delete():
    if len(stack)==0:
        print("The Stack Is Empty")
    else:
        stack.pop()
def insertion(x):
    if len(stack)==5:
        print("The Stack Is Full")
        #stack.pop()
    else:
        stack.append(x)

def display():
    for x in range(0,len(stack)):
        print("\n",stack[x])

    
while 7:
    print("\t","************Stack Oparation**************")
    print("1 For Push      :")
    print("2 For Pop       :")
    print("3 For Display   :")
    print("4 For Peek      :")
    print("5 For Exit      :")
    chs=int(input("Enter An Option :"))
    if chs==1:
        ele=int(input("Enter An Element:"))
        insertion(ele)
    elif chs==2:
        delete()
    elif chs==3:
        display()
    elif chs==4:
        print("The Peek Element Is :",stack[len(stack)-1])
    elif chs==5:
        exit(0)
    else:
        print("INVALID OPTION PLEASE TRY AGAIN")

else:
    print("Completed")
