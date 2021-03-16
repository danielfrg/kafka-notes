# %%
# This examples requires a local kafka broker and a topic created like:
# kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

topic = "test"

# %%

from confluent_kafka.admin import AdminClient
from confluent_kafka import Producer


# %% List topics
# Just to check we are in the right place

broker = "localhost:9092"
conf = {"bootstrap.servers": broker}

a = AdminClient(conf)

topics = a.list_topics()
topics.topics

# %% Create a producers

p = Producer(conf)


msgs = ["This is the first line", "of a long message"]

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


for line in msgs:
    try:
        # Produce line (without newline)
        p.produce(topic, line.strip(), callback=delivery_callback)

    except BufferError:
        print(
            "%% Local producer queue is full (%d messages awaiting delivery): try again\n"
            % len(p)
        )


print("%% Waiting for %d deliveries\n" % len(p))
p.flush()

# %% Consume using CLI

# Use this to consome the messages
# kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning

# If the command is still running we will see new messages appear on the output of that process
