降低np精度提升计算速度









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

