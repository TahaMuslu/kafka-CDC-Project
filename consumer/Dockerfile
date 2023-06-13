# FROM gradle:latest
# ENV TOPİC="X"
# WORKDIR /app
# COPY kafka-3.4.1-src .
# EXPOSE 5000
# CMD ["bin/zookeeper-server-start.sh", "config/zookeeper.properties", "&&", "bin/kafka-server-start.sh", "config/server.properties","&&","bin/kafka-topics.sh","--create","--topic",TOPİC,"--bootstrap-server","localhost:9092"]



FROM python:3
RUN pip install kafka-python
CMD [ "python3", "-u", "/kafkarun.py" ]