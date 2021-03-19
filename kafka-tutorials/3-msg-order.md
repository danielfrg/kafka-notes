# 3. How to maintain message ordering and no message duplication

Create topic with 2 partitions

```
kafka-topics --bootstrap-server localhost:9092 --topic myTopic --create --replication-factor 1 --partitions 2
```

Describe the topic

```
kafka-topics --bootstrap-server localhost:9092 --topic myTopic --describe
```

```
Topic: myTopic	PartitionCount: 2	ReplicationFactor: 1	Configs: segment.bytes=1073741824
	Topic: myTopic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
	Topic: myTopic	Partition: 1	Leader: 0	Replicas: 0	Isr: 0
```
