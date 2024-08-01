**Real Time Bitcoin Price Analysis using Kafka and Hadoop**
The program fetches real-time bitcoin data from the said URL through producer.py and pushes it into the topic.
Consumer recieves data from topic, does the necessary processing, appends it into Hadoop Distributed File System. (HDFS)
Mapper takes data from the HDFS, and pushes it into reducer. The reducer caclulates the average, and writes it into the file on local drive.
