#生产消息producer
from rocketmq.client import Producer, Message
import json

producer = Producer('PID-test')
producer.set_namesrv_addr('120.131.3.191:4324')  #rocketmq队列接口地址（服务器ip:port）
producer.start()

msg_body = {"id":"001","name":"test_mq","message":"abcdefg"}
ss = json.dumps(msg_body).encode('utf-8')

msg = Message('topic_name')   #topic名称
msg.set_keys('xxxxxx')
msg.set_tags('xxxxxx')
msg.set_body(ss)      #message body

retmq = producer.send_sync(msg)
print(retmq.status, retmq.msg_id, retmq.offset)
producer.shutdown()


# 消费消息consumer：
# 使用PullConsumer
from rocketmq.client import PullConsumer
consumer = PullConsumer('CID_test')
consumer.set_namesrv_addr('xxx.xxx.xxx.xxx:xxxxx')
consumer.start()

for msg in consumer.pull('topic_name'):
    print(msg.id, msg.body)
consumer.shutdown()
