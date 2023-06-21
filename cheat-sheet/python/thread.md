```python
from threading import Thread

class MyThread(Thread):
    def __init__(self, func, keyword):
        Thread.__init__(self)
        self.func = func   # 函数
        self.keyword = keyword   # 关键词
        print(self.keyword)
        self.result = []

    def run(self):
        self.result = self.func(*self.keyword)

    def get_result(self):
        return self.result



import time
def fun1(v1):
    time.sleep(5)
    print(v1)
    return v1
  
def fun2(v1,v2):
    time.sleep(5)
    print(v1,v2)
    return v1,v2
  
t1 = MyThread(func=fun1, keyword='1')
t2 = MyThread(func=fun2, keyword=('2','3'))
s = time.time()
t1.start()
t2.start()
# t1.join()
# t2.join()
e = time.time()
print(e-s) 
# >> 0.0016

t1.join() # 等待t1， 不join 就直接走下面的流程， 
e = time.time()
print(e-s) 
#  >> 5.0905



```







