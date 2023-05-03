marks=[]
total=0
for x in range(0,5):
    a=int(input("Enter Mark :"))
    marks.insert(x,a)
    total=marks[x]+total
per=total/5
for x in range(0,5):
    print("Subject(",x+1,")",'=',marks[x])
print("Total Marks   :",total)
print("Percentage    :",per,"%")
if per>=90 :
    print("Grade         :A+")
elif per>=80 and per<90:
    print("Grade         :A")
elif per>=70 and per<80:
    print("Grade         :B")
elif per>=60 and per<70:
    print("Grade         :C")
else:
    print("Grade         :D")

