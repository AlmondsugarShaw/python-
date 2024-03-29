#第三次上机作业2
total=int(input("总人数"))
n=0
CET4=0
CET6=0
unpassed=0
while n<total:
    print("请录入第",(n+1),"个学生的成绩")
    grade=input("英语等级是")
    if grade=="四级":
      CET4+=1
    if grade=="六级":
        CET6+=1
    else:
        unpassed+=1
    n+=1
print("|-------------------------------|")
print("|等级|人数|","比率|")
print("|-------------------------------|")
print("|四级|",CET4,"|",CET4/total,"|")
print("|-------------------------------|")
print("|六级|",CET6,"|",CET6/total,"|")
print("|-------------------------------|")
print("|其他|",unpassed,"|",unpassed/total,"|")
print("|-------------------------------|")
