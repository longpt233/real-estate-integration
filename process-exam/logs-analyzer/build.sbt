name := "log-analyzer"
version := "0.0.1"
scalaVersion := "2.12.1"

libraryDependencies ++= Seq(
"org.apache.spark" %% "spark-core" % "2.4.1" % "provided",
"org.apache.spark" %% "spark-streaming" % "2.4.1"
)
