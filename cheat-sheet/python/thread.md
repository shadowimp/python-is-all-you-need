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







### asyncio 

```python
import asyncio

async def boil_water():
    print("点火烧水")
    await asyncio.sleep(5)  # 模拟5秒等待，此时CPU可以去执行其他任务
    print("水开了！")

async def cut_fruit():
    print("开始切水果")
    await asyncio.sleep(2)
    print("水果切好了")

async def main():
    # 创建两个并行任务
    task1 = asyncio.create_task(boil_water())
    task2 = asyncio.create_task(cut_fruit())
    
    # 等待两个任务都完成
    await task1
    await task2

asyncio.run(main())
```







```python
import asyncio

async def boil_water(random_number):
    print("点火烧水")
    print(random_number)
    await asyncio.sleep(random_number)  # 模拟5秒等待，此时CPU可以去执行其他任务
    print("水开了！")
    return random_number
  
async def concurrent_task_with_timeout(coroutines):
    tasks = [asyncio.create_task(coro) for coro in coroutines]
    results = [None] * len(coroutines) 
    done , pending = await asyncio.wait(tasks)
    for task in done:
        index = tasks.index(task)
        results[index] = task.result()
    return results 
```

