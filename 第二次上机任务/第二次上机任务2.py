#第二次上机任务2
total=int(input("总人数"))
CET4circulation=0
CET6circulation=0
CET4passed=0
CET4unpassed=0
CET6passed=0
CET6unpassed=0
while CET4circulation<total:
    score=int(input("CET4score"))
    if 425<=score:
      CET4passed+=1
    else:
        CET4unpassed+=1
    CET4circulation+=1
while CET6circulation<total:
    score=int(input("CET6score"))
    if 425<=score:
      CET6passed+=1
    else:
        CET6unpassed+=1
    CET6circulation+=1
print("|-------------------------------|")
print("|      |通过人数|","通过比率|")
print("|-------------------------------|")
print("| 四级 |",CET4passed,"    |",CET4passed/total,"|")
print("|-------------------------------|")
print("| 六级 |",CET6passed,"    |",CET6passed/total,"|")
print("|-------------------------------|")
