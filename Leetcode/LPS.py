#-*-coding:utf-8-*- 
def fun(s):  #检测一个字符串是否是回文字符串，时间复杂度为n
	if (len(s)<2): 
		return False
	for i in range(len(s)//2): 
		if s[i] != s[len(s)-1-i]: 
			return False 
	return True 

print(fun('abc'))
print(fun('absdfdsba'))
print(fun('asfhiihfsa'))
print(fun('a'))


#获得一个字符串的所有子串
def get_SubString(s): 
	return [s[j:j+i+1]for i in range(len(s)) for j in range(len(s)-i)]

print(get_SubString('adf'))

print('*'*10+'(main)'+'*'*10)

#longest palindromic substing 最大回文子串 蛮力破解 Time:O(n^3) Space:O(n^2)
def lmp_BruteForce(s):
	nums = get_SubString(s)
	for item in nums: 
		if fun(item): 
			return item 
	return None 

print(lmp_BruteForce('babad'))
print(lmp_BruteForce('cbbd'))
print(lmp_BruteForce('adf'))






