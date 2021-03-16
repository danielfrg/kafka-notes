# %%
# This examples requires a local kafka broker and a topic created like:
# kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 5 --topic test.p5

# Reset topic with:
# kafka-topics --delete --bootstrap-server localhost:9092  --topic test.p5

topic = "test.p5"

# %%

from confluent_kafka.admin import AdminClient
from confluent_kafka import Producer

# %% List topics
# Just to check we are in the right place

broker = "localhost:9092"
conf = {"bootstrap.servers": broker, "acks": "all"}

a = AdminClient(conf)

topics = a.list_topics()
topics.topics

# %%

# Optional per-message delivery callback (triggered by poll() or flush())
# when a message has been successfully delivered or permanently
# failed delivery (after retries).
def delivery_callback(err, msg):
    if err:
        print("%% Message failed delivery: %s\n" % err)
    else:
        print(
            "%% Message delivered to %s [%d] @ %d\n"
            % (msg.topic(), msg.partition(), msg.offset())
        )


p = Producer(conf)

# %% Create a producers

msgs = [
    "1",  # Partition 3
    "2",  # Partition 2
    "3",  # Partition 1
    "4",  # Partition 3
    "5",  # Partition 1
    "300",  # Partition 4
    "3000000000",  # Partition 0
    "2000000000",  # Partition 1
    "1000000000",  # Partition 3
]

for line in msgs:
    try:
        # Produce line (without newline)
        p.produce(topic, line.strip(), key=line, callback=delivery_callback)

    except BufferError:
        print(
            "%% Local producer queue is full (%d messages awaiting delivery): try again\n"
            % len(p)
        )

    # This is to make it basically syncronous
    p.flush()


# %% Consume using CLI

# Use this to read messages from a particular partition:
# kafka-console-consumer --bootstrap-server localhost:9092 --topic test.p5 --from-beginning --partition 3

# If the command is still running we will see new messages appear on the output of that process as we send more messages

# %%
