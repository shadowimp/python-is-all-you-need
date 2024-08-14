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





### kafka

```python
from kafka import KafkaConsumer, KafkaProducer


# 设置Kafka消费者参数
bootstrap_servers = ''  # Kafka服务器地址
topic = ''  # 你想要消费的主题名
group_id = ''  # 消费者组ID


# 创建Kafka消费者
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    group_id=group_id,
    enable_auto_commit=True,  # 自动提交偏移量
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # 假设消息是json格式
)=
print("开始消费Kafka消息...")
for message in consumer:
    # 解析并处理消息
    msg = message.value
    print(msg)
    
    
# 设置Kafka者参数
topic_name = ''
bootstrap_servers = '' 
producer = KafkaProducer(
bootstrap_servers=bootstrap_servers,
        sasl_mechanism = "PLAIN",
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # 确保消息是字节串，适用于字符串类型的消息
      )
message = {"id": ""}
m = json.dumps(message)
# 异步发送消息
producer.send(topic_name, message)
# 强制同步发送，确保消息被发送出去
producer.flush()
# 关闭生产者连接
producer.close()
    

```

