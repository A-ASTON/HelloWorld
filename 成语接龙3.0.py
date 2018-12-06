def judge(list_chengyu):#判断用户输入的成语是否在词库中
    chengyu = input('在此输入成语：')
    if chengyu in list_chengyu:    #如果在，则进行接龙
        for line in list_chengyu:#for循环，从词库中寻找能接上的成语
            if list(line)[0] == list(chengyu)[-1]:
                print(''.join(list(line)))
                list_chengyu.remove(chengyu and line)#在列表中删除使用过的成语
                return (list_chengyu)
        print('你太厉害了！电脑都斗不过你！')#电脑寻找不到能接上的成语，玩家获胜
    else:
        print('你太菜了，这都输了！')#玩家输入的成语不在词库中，则游戏结束
from random import *
with open('chengyutianci.txt', 'r') as file:
    list_chengyu = [line.rstrip('\n') for line in file if len(line) > 2]#从词库中获取成语（不存在大写字母），并放入列表中
print('开始你的成语接龙吧！\n' + choice(list_chengyu))#随机从词库中获取成语
while judge(list_chengyu) != None:
    continue

