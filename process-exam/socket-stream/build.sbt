name := "socket-stream"
version := "0.0.1"
scalaVersion := "2.11.12"
libraryDependencies ++= Seq(
"org.apache.spark" %% "spark-core" % "2.4.1" % "provided",
"org.apache.spark" %% "spark-streaming" % "2.4.1"
)
