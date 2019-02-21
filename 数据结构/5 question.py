#-*-coding:utf-8-*-
# 使用for，while，和递归写出三个函数来计算给定数列的总和

#1. for 
def sum_for(x):
	sum = 0
	for i in range(len(x)):	
		sum = sum + x[i]
	return sum

print(sum_for([1,3,4,9]))

#2. while 
def sum_while(x):
	sum = 0 
	i = 0
	while(i < len(x)):
		sum = sum + x[i]
		i = i +1
	return sum
print(sum_while([1,3,4,9]))

#3. 递归 f(n) = f(n-1) + f()
def sum_recursive(x):
	if (len(x) == 0):
		return 0 
	else :
		return x.pop(len(x)-1)+sum_recursive(x) 
print (sum_recursive([1,2,3,4]))
