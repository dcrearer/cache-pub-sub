import redis
import os

CLUSTER = os.environ["CLUSTER"]

# Connect to Redis
r = redis.StrictRedis(host=CLUSTER, port=6379, ssl=True, db=0)

channel_name = 'channel01'

# Create a PubSub object
pubsub = r.pubsub()

# Subscribe to the channel
pubsub.subscribe(channel_name)

print(f"Subscriber started. Listening on '{channel_name}'...")

try:
    # Listen for messages
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = message['data'].decode('utf-8')
            print(f"Received: '{data}'")
except KeyboardInterrupt:
    print("\nSubscriber stopped.")
finally:
    pubsub.unsubscribe(channel_name)
    print("Unsubscribed from channel.")