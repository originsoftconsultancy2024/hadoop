from kafka import KafkaConsumer
import json
import subprocess

bootstrap_servers = ['localhost:9092']
topics = ['topic1', 'topic2', 'topic3']  # List of your desired topics
hdfs_path = '/input/bit_coin.txt'  

# Function to append data to HDFS file using Hadoop command
def append_to_hdfs(data):

    command = ['hadoop', 'fs', '-appendToFile', '-', hdfs_path]
    # Execute command and pass data through stdin
    subprocess.run(command, input=data.encode('utf-8'), check=True)

# Create a Kafka consumer instance and subscribe to all three topics
consumer = KafkaConsumer(*topics, bootstrap_servers=bootstrap_servers,
                        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

while True:
    for message in consumer:
        topic, price_data = message.topic, json.dumps(message.value)
        # Append data to HDFS file
        append_to_hdfs(price_data + '\n')
        print(f'Received and appended to HDFS from topic {topic}: {price_data}')

