```python
import redis

redis_conn = redis.Redis(host='127.0.0.1', port= 6379, password= 'your pw', db= 0)


# set 
redis_conn.set('name_2', 'Zarten_2')


# get 
v = redis_conn.get('name_1')
print(v)

```



