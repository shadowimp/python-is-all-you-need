import os
import numpy as np
import matplotlib.pyplot as plt

data_path = './data'
data_filenames = ['2017-q1.scv','2017-q2.csv','2017-q3.csv','2017-q4.csv']

def data_collect(data_path,data_filenames):
	data_arr_list = []

	for data_filename in data_filenames:
		data_file = os.path.join(data_path,data_filename)		#路径拼接
		data_arr = np.loadtxt(data_file,delimiter=',', dtype = 'str ', skiprow = 1 ) # 跳过第一行
		# data_arr.shape = (646586,9)
		data_arr_list.append(data_arr)
	return data_arr_list

def data_process(data_arr_list):
	duration_in_min_list  = []

	for data_arr in data_arr_list:
		#需要所有数据的第0列,骑行时间
		duration_str_col = data_arr[:,0]

		#去掉双引号,向量化操作。
		duration_in_ms = np.core.defchararray.replace(duration_str_col,'"','')

		#将字符型转换为浮点型,毫秒转分钟
		duration_in_min = duration_in_ms.astype('float') / 1000 / 60

	return duration_in_min_list


def data_analyze(duration_in_min_list):
	duration_mean_list = [ ]
	for idx, duration in enumerate(duration_in_min_list):
		duration_mean = np.mean(duration)
		duration_mean_list.append(duration_mean)


	return duration_mean_list

def data_show(duration_mean_list ):
	plt.figure()
	plt.bar(range(len(duration_mean_list)), duration_mean_list )
	plt.show ()

def main():
	data_arr_list = data_collect()
	duration_list  = data_process(data_arr_list)
	duration_in_min_list = data_analyze(duration_list)
	data_mean_list = data_analyze(duration_in_min_list)
