#-*-coding:utf-8-*-

'''
python脚本 模糊查询文件名。
输入： 文件的关键字 文件的类型
输出： 文件的完整路径

'''
import os  # os模块（operation system)与系统相关的库函数
def find_path(path,name,type):
	files = os.listdir(path)
	for f in files:
		if name in f and f.endswith(type):
			print(f)


path = "/Users/mac/Desktop/algorithm-git"
find_path(path,'me','.py')
