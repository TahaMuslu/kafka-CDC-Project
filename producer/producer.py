import os
from kafka import KafkaProducer
from pymongo import MongoClient
import time

# MongoDB configuration
mongo_uri = 'mongodb://mongo:27017/'
mongo_db = os.environ['MONGODB_DB']
mongo_collection = os.environ['MONGODB_C']

# Kafka configuration
kafka_bootstrap_servers = os.environ['KAFKA_BROKERCONNECT']
kafka_topic = os.environ['TOPIC']

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)

# Connect to MongoDB
mongo_client = MongoClient(mongo_uri, replicaSet='mongoSet')
mongo_db = mongo_client[mongo_db]
collection = mongo_db[mongo_collection]

# Start change stream
change_stream = collection.watch()

for change in change_stream:
    if change["operationType"] == "insert":
        document = change["fullDocument"]
        message = str(document)  # Convert the document to string format
        producer.send(kafka_topic, value=message.encode('utf-8'))
        producer.flush()
        print("Mesaj Gönderildi:", document)

# Close the MongoDB and Kafka connections
mongo_client.close()
producer.close()
