import asyncio
from aiokafka import  AIOKafkaConsumer
from config.config import settings


async def consume():
    # Create Kafka consumer
    consumer = AIOKafkaConsumer(
        settings.TOPIC_NAME,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,  
        group_id='my-group',  # Consumer group ID
        auto_offset_reset='earliest'  # Start reading from the earliest message if no offset is found
    )
    await consumer.start()

    try:
        while True:
            # Poll messages asynchronously
            async for message in consumer:
                print(f"Received message: {message.value.decode('utf-8')} "
                      f"from partition {message.partition} and offset {message.offset}")
    except asyncio.CancelledError:
        print("Consumer task was cancelled")
    finally:
        await consumer.stop()

