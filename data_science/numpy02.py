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








def main():
	data_collect_and_process()
	data_analyze()
	data_save_and_show()
