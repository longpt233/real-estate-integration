## Run programming
```
sbt clean package
spark-submit --class SocketStream --master local[2] target/scala-2.11/socket-stream_2.11-0.0.1.jar
```
