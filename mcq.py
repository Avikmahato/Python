from termcolor import colored
from colorama import Fore,Back
import os
questions=[[["(1) What is the result of cmp(3,1)?","b"],["a) 0","b) 1","c) True","d) False"]],[["(2) What does len() do?","d"],["a) Determine the lenght of a string","b) Determine the lenght of a  list","c) Determine the lenght of an array","d) All Of Above"]],[["(3) Which of the following statements are true?\n\n(i)Python is a strongly types language.\n(ii) The as keyword is used to createan alias of a modulere in python.\n(iii) Slicing operator will work on set.\n(iv) Lambda functions are syntactically restricted to single line.","b"],["a) i,ii and iv are true","b) All are true","c) ii and iv are true","d) ii,iii and iv are true"]],
        [["(4) What will be the output after executing the following python script ?\nd1={1:'A',2:'B',3:'C'}\nd2=d1.copy()\nprint(id(d1)==id(d2))","b"],["a) True","b) False","c) Dictionary class does not have copy() method","d) None of the above"]],[["(5) What will be the value of the following ?\n\tfloat(22//3+3/3)","b"],["a) 8.00","b) 8.0","c) 8","d) Error"]],[["(6) What will be the output of the follwing Python program?\ndef additem(list param):\nlist param+=[1]\nmy list=[1,2,3,4],\nadditem(my list)\nprint(len(my list))","a"],["a) 5","b) 8","c) 2","d) 1"]],[["(7) What is the value of the following expression ?\n2+4.00,2**4.0","b"],["a) (6,16)","b) (6.0, 16.0)","c) (6.00 , 16.0 )","d) (6.00 , 8.0)"]],[["(8) Write the output of the given:\nX=int(43.55+2/2)","b"],["a) 43","b) 44","c) 22","d) 23"]],[["(9) What will be the output after executing the following python script?\n\nfor x in range(0,4):\n\tprint(x,end=',')","b"],["a) 0,1,2,3,4,","b) 0,1,2,3,","c) 1,2,3,4,","d) 1,2,3"]],
           [["(10) Consider a list variable having the follwoing data\nmylist=[6,4,2,110].Which of the following statement is correct way to sort the list?\nstatement 1:sort(mylist)\nstatement 2:mylist.sorted()","b"],["a) Statement 1 is correct and Statement 2 is wrong","b) Statement 1 is wrong and Statement 2 is correct","c) Both Statement 1 and Statement 2 is wrong","Both Statement 1 and Statement is correct"]],[["(11) Which of the python sequence in python is immutable?","a"],["a) Set","b) List","c) Tuple","d) Dictionary"]],[["(12) What are the values of the following Python expression ?\n\t2**(3**2)\n\t(2**3)**2\n\t2**3**2","d"],["a) 512,64,64","b) 512,512,512","c) 64,64,64","d) 512,64,512"]],[["(13) What will be the value of x after executing the following Pyhton Expression ?\n\tx=15*4-8/2","a"],["a) 56","b) 56.0","c) 0.0","d) 26.0"]],[["(14) What will be the value of x after execurting the following Python Expression ?\nx=4 or 3/0","a"],["a) 4","b) True","c) False"," Error"]],[["(15) What will be the value of x after executing the following Python Expression?\n\tx=bool(4)\n","a"],["a) True","b) False","c) Error","d) 0b100"]],
           [["(16) What will be the output of the following code snoppet?\nprint(2 ** 3 + (5 + 6)**(1 + 1))","d"],["a) 8","b) 121","c) 130","d) 129"]],[["(17) What will be the output of the following python code?\na = [1,2,3]\na = tuple(a)\na[0] = 2\nprint(a)","c"],["a) [2,2,3]","b) (2,2,2)","c) Error","d) (1,2,3)"]]]
point=0
corr=[]
print(Fore.GREEN+"\t************Student Details***************\n")
name=input(Fore.BLUE+"   Student Name          :")
reg=input("   Registration  No :")
roll=input("   Roll            :")
no=input("   No                :")
for i in range(len(questions)):
    print(Fore.RED+"\t\t\t\t\tMARKS :",point)
    print(colored(questions[i][0][0],'cyan'))
    for k in questions[i][1]:
        print('\t',colored(k,'yellow'))
    rep=input(colored(Fore.MAGENTA+"Choose An Option :"))
    if rep==questions[i][0][1]:
        point+=2
        corr.append(1)
        print(colored("Your Answer Is Correct",'black','on_green'))
    else:
        print(colored("*******************WRONG ANSWER******************",'blue','on_red'))
        corr.append(0)
if point>=30:
    point=30
os.system('cls')
print(colored("******************MarkSheet*******************",'red','on_green'))
print(Fore.LIGHTCYAN_EX+"Name                                :",name)
print("Registration                        :",reg)
print("Roll                                :",roll)
print("NO                                  :",no)
print("Marks                               : ",point)
print("Percentile                          : %.2f%%"%(point/3),'\n\n')
for x in range(0,len(corr)):
    print("Question No  ",x+1,':')
    if corr[x]==1:
        print("-------->Correct")
    else:
        print("-------->Wrong")