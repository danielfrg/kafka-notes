# 1. The basics

Create a topic

```
kafka-topics --create --topic example-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

Create consumer

```
kafka-console-consumer --bootstrap-server localhost:9092 --topic example-topic
```

Create a producer

```
kafka-console-producer --bootstrap-server localhost:9092 --topic example-topic
```

Type on this terminal and see the output on the consumer one

Now read all the records (can be in another terminal)

```
kafka-console-consumer --bootstrap-server localhost:9092 --topic example-topic --from-beginning
```

If you write on the producer both consumers will get the messages.

## key-value pairs

Create a new producer that parses keys

```
kafka-console-producer --bootstrap-server localhost:9092 --topic example-topic --property parse.key=true --property key.separator=":"
```

Create a producer that will print the keys

```
kafka-console-consumer --bootstrap-server localhost:9092 --topic example-topic --from-beginning --property print.key=true --property key.separator="-"
```
