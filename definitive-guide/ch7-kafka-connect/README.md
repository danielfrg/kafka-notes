
List connectors:

```
curl http://localhost:8083/connector-plugins
```

Create Source on a `kafka-config-topic` topic

```
curl -X POST -d @file-source.json http://localhost:8083/connectors --header "Content-Type:application/json"
```

Check created topic:

```
$ kafka-console-consumer --bootstrap-server=localhost:9092 --topic kafka-config-topic --from-beginning

{"schema":{"type":"string","optional":false},"payload":"#confluent.telemetry.enabled=true"}
{"schema":{"type":"string","optional":false},"payload":"#confluent.telemetry.api.key=<CLOUD_API_KEY>"}
{"schema":{"type":"string","optional":false},"payload":"#confluent.telemetry.api.secret=<CCLOUD_API_SECRET>"}
```

Delete source (if needed)

```
curl -X DELETE http://localhost:8083/connectors/load-kafka-config
```


Create Sink reading from the topic and writting to the local file

This file is relative to where Kafka Connect is running

```
curl -X POST -d @file-sink.json http://localhost:8083/connectors --header "Content-Type:application/json"
```

Delete sink (if needed)

```
curl -X DELETE http://localhost:8083/connectors/dump-kafka-config
```
