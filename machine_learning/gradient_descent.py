import numpy as np

def load_data():
    data_mat = [] #训练数据
    label_mat = [] #标签
    label_dict = {'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3} #将label值转变成数值量便于计算损失
    f = open('Iris.txt')
    for line in f.readlines():
        line_arr = line.strip().split(',') #先strip后split
        data_mat.append([float(x) for x in line_arr[:-1]])  #将string类型的数据变成浮点型，每个数据包含四个feature
        label_mat.append(label_dict[line_arr[-1]]) #最后一列是数据的标签
    return data_mat , label_mat


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def gradient_descent(data, label):  #梯度下降
    dataMatrix = np.mat(data)
    labelMatrix = np.mat(label).transpose()
    m, n = np.shape(dataMatrix)
    alpha = 0.001
    maxCycles = 200 #最大的迭代次数

    weights = np.ones((n,1)) #weights 是一个n行1列的列向量
    for k in range(maxCycles):
        z = sigmoid(dataMatrix * weights)
        error = (labelMatrix - z)
        weights -= alpha * dataMatrix.transpose() * error

    return weights

data,label = load_data()
print(gradient_descent(data,label))
