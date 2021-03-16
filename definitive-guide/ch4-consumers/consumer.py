# %%

# Create a topic with some partitions
# kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 5 --topic test.p5

# %%

import logging

from confluent_kafka import Consumer, KafkaException

# %%

broker = "localhost:9092"
group = "my-group-3"
topics = ["test.p5"]

conf = {
    "bootstrap.servers": broker,
    "group.id": group,
    "session.timeout.ms": 6000,
    # "auto.offset.reset": "latest",  # default
    "auto.offset.reset": "earliest",
}

# %%

# Create logger for consumer (logs will be emitted when poll() is called)
logger = logging.getLogger("consumer")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)-15s %(levelname)-8s %(message)s"))
logger.addHandler(handler)

# Create Consumer instance
# Hint: try debug='fetch' to generate some log messages
c = Consumer(conf, logger=logger)


def print_assignment(consumer, partitions):
    print("Assignment:", partitions)


# Subscribe to topics
c.subscribe(topics, on_assign=print_assignment)

# %% Consume

try:
    while True:
        msg = c.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            # Proper message
            print(
                "%s [%d] at offset %d with key %s:"
                % (msg.topic(), msg.partition(), msg.offset(), str(msg.key()))
            )
            print(msg.value())

            import time

            time.sleep(1)

except KeyboardInterrupt:
    print("%% Aborted by user\n")

finally:
    # Close down consumer to commit final offsets.
    c.close()

# %%
