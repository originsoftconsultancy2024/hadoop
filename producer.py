import requests
import json
from kafka import KafkaProducer
from time import sleep

url = 'https://api.coinbase.com/v2/prices/btc-usd/spot'
bootstrap_servers = ['localhost:9092']
topic1 = 'topic1'
topic2 = 'topic2'
topic3 = 'topic3'
producer1 = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))
producer2 = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))
producer3 = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))                      

while True:
    sleep(2)
    price_data = requests.get(url).json()
    
    if float(price_data['data']['amount']) < 63400:
    
    	producer1.send(topic1, value=price_data)
    	print('Price sent to Kafka by producer 1: ', price_data)
    	
    elif float(price_data['data']['amount']) > 63400 and float(price_data['data']['amount']) < 63500:
    
    	producer2.send(topic2, value=price_data)
    	print('Price sent to Kafka by producer 2: ', price_data)
    	
    else:	
        
    	producer3.send(topic3, value=price_data)
    	print('Price sent to Kafka by producer 3: ', price_data)
