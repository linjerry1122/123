score=[]
total = inscore =0
while( inscore!=-1 ):
    inscore=int(input("輸入成績"))
    score.append(inscore)
for i in range(0, len(score)-1):
    total = score[i]+total
avg=total/(len(score)-1)
print("共%d位學生\n總分為%d\n平均分數為%5.1f" %( len(score)-1,total, avg))