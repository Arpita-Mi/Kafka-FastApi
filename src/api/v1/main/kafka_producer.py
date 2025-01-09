import asyncio
from aiokafka import AIOKafkaProducer
from config.config import settings

async def produce(msg):
    # Create Kafka producer
    producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()

    try:
        result  = await producer.send_and_wait(settings.TOPIC_NAME, value=msg.message.encode())
        return {
            "status": "Message sent",
            "topic": result.topic,
            "partition": result.partition,
            "offset": result.offset,
            "key": "",
            "value": msg.message
        }
    finally:
        await producer.stop()