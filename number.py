#猜数字
import random
number=random.randint(0,1000)
i=input('请输入数字')
a=int(i)
while a!=number:
	if a>number:
		print ('大了')
	elif a<number:
		print ('小了')
	else :
		print('正确')
		break
	i=input('请从新输入数字')
	a=int(i)
print('游戏结束')
