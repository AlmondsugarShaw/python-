#第二次上机作业1
total=int(input("总人数"))
circulation=0#循环次数
excellent=0#优秀人数
good=0#良好人数
medium=0#中等人数
passed=0#及格人数
unpassed=0#不及格人数
maxscore=0
minscore=100
totalscore=0
while circulation<total:
    score=int(input("score"))
    if 90<=score<=100:
       excellent+=1
    elif score>=80:
        good+=1
    elif score>=70:
        medium+=1
    elif score>=60:
        passed+=1
    else:
        unpassed+=1
    circulation+=1
    maxscore=max(maxscore,score)
    minscore=min(minscore,score)
    totalscore+=score
print("|-------------------------------|")
print("|      |人数|","    比率   |")
print("|-------------------------------|")
print("| 优秀 |",excellent,"|",excellent/total,"|")
print("|-------------------------------|")
print("| 良好 |",good,"|",good/total,"|")
print("|-------------------------------|")
print("| 中等 |",medium,"|",medium/total,"|")
print("|-------------------------------|")
print("| 及格 |",passed,"|",passed/total,"|")
print("|-------------------------------|")
print("|不及格|",unpassed,"|",unpassed/total,"|")
print("|------------------------------|")
print("|最高分|",maxscore,"|最低分|",minscore,"|平均分|",totalscore/total,"|")
print("|------------------------------|")
