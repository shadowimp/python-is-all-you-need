```python
import redis

redis_conn = redis.Redis(host='127.0.0.1', port= 6379, password= 'your pw', db= 0)


# set 过期时间, -1代表不过期
redis_conn.set('name_2', 'Zarten_2',ex=60*60)



# get 
v = redis_conn.get('name_1')
print(v)


# exist
redis_conn.exists('name')

# delete 
redis_conn.delete('name')

```



