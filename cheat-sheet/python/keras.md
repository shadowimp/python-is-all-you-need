```python
keras.layers.Input()

输入

from keras.layers import Input
x = Input(shape=(32,))
shape: 函数的输入形状，数据的形式为元组(元组参数要为int型)，不包含batch大小的那个维度
  

  
  
concatenate
拼接两种类型的tensor


concatenate([1,2,3],[10,20,30])


#dense 
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
model.add(Dense(13))

f_size = 2 
x_in = Input(shape=(784,))
f = Dense(f_size)(x_in)


#lambda  如果某一层需要通过一个函数去变换数据，那利用keras.layers.Lambda()这个函数单独把这一步数据操作命为单独的一Lambda层。

lambda(slice, output_shape=(4,1),arguments={'index':0})(a)





```

