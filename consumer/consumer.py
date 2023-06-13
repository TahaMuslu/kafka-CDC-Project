from kafka import KafkaConsumer
import os
# Kafka configuration
kafka_bootstrap_servers = os.environ['KAFKA_BROKERCONNECT']
kafka_topic = os.environ['TOPIC']
kafka_group_id = 'group'+os.environ['CONSUMER_ID']

# Create a Kafka consumer
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_bootstrap_servers,
    group_id=kafka_group_id
)

# Start consuming messages
for message in consumer:
    received_message = message.value.decode('utf-8')
    print('Consumer{'+os.environ['CONSUMER_ID'] +
          '}-- '+'Received message:', received_message)

# Close the Kafka consumer
consumer.close()
