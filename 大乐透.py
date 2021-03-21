
import random
def yao_hao(total,top):#形参total为选几个号码，形参top为选择范围1~top
    lucky=[]
    n=0
    while (n<total):
        num=random.randint(1,top)#在1~top的范围内随机选一个数num
        if not num in lucky:#如果上一行所选的数字不在lucky数列里
            lucky.append(num)#则把num添加岛数列lucky中
            n=n+1
    lucky.sort()#对lucky数列进行排序
    return (lucky)#函数范围一个数列lucky

print("前区：",yao_hao(5,35),"后区：",yao_hao(2,12))