

```python
import numpy as np
#邻接矩阵表
A = np.matrix([
    [0, 1, 0, 0],
    [0, 0, 1, 1], 
    [0, 1, 0, 0],
    [1, 0, 1, 0]],
    dtype=float
)
A.shape

# 抽取特征 
X = np.matrix([[i,-i] for i in range(A.shape[0])] , dtype = float)


# A为邻接矩阵， X为输入特征
A*X
```



HA - histroy average 历史平均

````python
# History average
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import time

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.optim as optim
import torch.nn.functional as F
from util import RMSELoss

city = 'Beijing'
OD = sio.loadmat('../data/OD_'+city+'.mat')['OD']
OD_train = OD[:, :, :24*7*4]
OD_test = torch.FloatTensor(OD[:, :, 24*7*4:])

N = OD_train.shape[0]
T = OD_train.shape[2]

OD_pre = torch.FloatTensor(np.mean(OD_train.reshape((N, N, int(T/(7*24)), 7*24)),2))

test_RMSE = RMSELoss()
test_MSE = torch.nn.MSELoss()
test_MAE = torch.nn.L1Loss()
test_rmse = test_RMSE(OD_pre, OD_test)
test_mse = test_MSE(OD_pre, OD_test)
test_mae = test_MAE(OD_pre, OD_test)
# test_rmse = test_RMSE(OD_pre[:,:,0], OD_test[:,:,0])
# test_mse = test_MSE(OD_pre[:,:,0], OD_test[:,:,0])
# test_mae = test_MAE(OD_pre[:,:,0], OD_test[:,:,0])

print("rmse: %.3f mse: %.3f mae: %.3f"%(float(test_rmse), float(test_mse), float(test_mae)))
````





```python
argmin

np.argmin(x,axis=None)
# 返回axis方向最小值的index

a = array([[3, 4, 6],
       [8, 2, 1]])

>>> np.argmin(a, axis=0)
array([0,1,2])

>>> np.argmin(a,axis=0)
array([0,2])

>>>np.argmin(a,axis=None)
5







```

