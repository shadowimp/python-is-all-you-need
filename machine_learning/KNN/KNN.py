#-*-coding:utf-8-*-

'''
K—Nearest Neighbors 
For every point in our dataset:
	calucute the distance between x and the current point 
	sort the distances 
	take k lowest distance 
	find the majority class among the k items 
	return the majortity as the prediction 
输入： dataset , labels , x , k 
输出： label 

'''
from numpy import * 
from operator import itemgetter
from os import listdir 

# Create Dataset 
group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])  # the data is  2 dimension vector 
labels = ['A','A','B','B']  

def classify(dataset, labels, x ,k):  # x is just like the data is a 2 dimension vector 
	dataset_size = dataset.shape[0]  # array.shape is the tuple (rows,columns)
	diffMat = tile(x,(dataset_size,1)) - dataset 
	distances = ((diffMat**2).sum(axis=1))**0.5 # axis=1 意思是按列相加
	sorted_distances = distances.argsort() # argsort 是将数组的索引按对元素的大小从小到大排列
	
	class_count = {} #key是标签，value是
	for i in range(k):
		v = labels[sorted_distances[i]]
		class_count[v] = class_count.get(v,0) + 1 # get（v,0):如果字典的key中有v，返回dict[v] 否则返回0
	print(class_count)
	sorted_class_count = sorted(class_count.items(),key = itemgetter(1),reverse = True ) #items迭代字典中的元素, a(itemgetter(1)) 意思是获得a的index为1的元素， reverse = True (升序)
	print(sorted_class_count)
	return sorted_class_count[0][0] #获得列表中的第一个值（最小值） 
  

print(classify(group,labels,[0,0],3))
	


def dating_data(filename):
	fr = open(filename)
	n = len(fr.readlines())
	train_mat = zeros((n,3))
	labels = []
	fr = open(filename)
	index = 0 
	for line in fr.readlines():
		data = line.strip().split('\t')
		train_mat[index,:] = data[0:3]
		labels.append(data[-1])
		index += 1 
	return train_mat , labels


def normalize(data):  
	min_data = data.min(0)
	max_data = data.max(0)
	ranges = max_data - min_data 
	normalize_data = zeros(shape(data))
	m = data.shape[0]
	normalize_data = (data - tile(min_data,(m,1)))/ tile(ranges,(m,1))

	return normalize_data, ranges,min_data

def dating_test():
	h = 0.1 
	train_mat,labels = dating_data('datingTestSet.txt')
	normalize_data,ranges,min_data = normalize(train_mat)
	m = normalize_data.shape[0]
	n = int(m*h)
	error = 0.0 
	for i in range(n):
		classifier_result = classify(normalize_data[n:m],labels[n:m],normalize_data[i,:],3)
		# print('the classifier came back with:%s ,the real answer is %s'%(classifier_result,labels[i]))

		if classifier_result != labels[i] :
			error = error + 1.0 #错误个数+1 


	return error/float(n) #错误的个数/总数 即是错误率 

print(dating_test())


print("*"*30)
def predict_person():
	result_list = ['low','middle','high']
	train_mat,labels = dating_data('datingTestSet.txt')
	normalize_data,ranges,min_data = normalize(train_mat)
	in_data = array([30000,8.2,0.8])
	classifier_result = classify(normalize_data,labels,(in_data-min_data)/ranges,3)
	print(classifier_result)
predict_person()


def img2vector(filename):
	result_vector = zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		line = fr.readline()
		for j in range(32):
			result_vector[0,32*i+j] = int(line[j])
	return result_vector

file_digits_name = '0_1.txt'
print(img2vector(file_digits_name)[0,34:78])

def handwriting():
	labels = []
	train_file_list = listdir('trainingDigits')
	test_file_list = listdir('testDigits')
	m_train = len(train_file_list)
	train_mat = zeros((m_train,1024))
	for i in range(m_train):
		file_raw_name = train_file_list[i]
		file_name = file_raw_name.split('.')[0]
		label = int(file_name.split('_')[0])
		labels.append(label)
		train_mat[i,:] = img2vector('trainingDigits/%s' % file_raw_name) #文件夹操作

	error_count = 0
	m_test = len(test_file_list)
	for i in range(m_test):
		file_raw_name = test_file_list[i]
		file_name = file_raw_name.split('.')[0]
		label = file_name.split('_')[0]
		ve = img2vector('testDigits/%s'%file_raw_name)
		classifier_result = classify(train_mat,labels,ve,3)
		if classifier_result != file_name :
			error_count += 1 
	return error_count/m_test

print(handwriting())






