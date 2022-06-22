import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.streaming.dstream.DStream
import org.apache.spark.streaming.Duration
import org.apache.spark.streaming.Seconds

object SocketStream {
    def main(args : Array[String]){
	val conf = new SparkConf().setAppName("Socket-Stream")
	val ssc = new StreamingContext(conf, Seconds(1))
	val lines = ssc.socketTextStream("localhost", 7777)
	val errorLines = lines.filter(_.contains("error"))
	errorLines.print()
	ssc.start()
	ssc.awaitTermination()
    }
}
