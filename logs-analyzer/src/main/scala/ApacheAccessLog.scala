case class ApacheAccessLog(
	ipAddress: String, 
	clientIdentd: String,
	userId: String, 
	dateTime: String, 
	method: String, 
	endpoint: String, 
	protocal: String, 
	responseCode: Int, 
	contentSize: Long){
}

object ApacheAccessLog {
    val PATTERN = """^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+)""".r
    def parseLogLine(log: String): ApacheAccessLog = {
	log match {
	    case PATTERN(ipAddress, 
		clientIdentd, 
		userId,
		dateTime,
		method, 
		endpoint, 
		protocol, 
		responseCode, 
		contentSize) => new ApacheAccessLog(ipAddress,
					clientIdentd, 
					userId, 
					dateTime, 
					method, 
					endpoint, 
					protocol, 
					responseCode.toInt, 
					contentSize.toLong)
	    case _ => throw new RuntimeException(s"""Cannot parse log line $log""")
	}
    }
}
