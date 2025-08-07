import redis
import time
import os

CLUSTER = os.environ["CLUSTER"]

# Connect to Redis
r = redis.StrictRedis(host=CLUSTER, port=6379, ssl=True, db=0)

channel_name = 'channel01'

print(f"Publisher started. Publishing messages to '{channel_name}'...")

for i in range(500000):
    message = f"Hello from publisher! Message {i+1}"
    r.publish(channel_name, message)
    print(f"Published: '{message}'")
    time.sleep(.5)

print("Publisher finished.")