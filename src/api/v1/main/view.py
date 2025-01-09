from src.api.v1.main.kafka_consumer import consume
from src.api.v1.main.kafka_producer import produce
from src.api.v1.main.schema import Message
from fastapi import status , FastAPI , APIRouter
import asyncio
router = APIRouter()



@router.post('/send_message', summary="kafka message broker" , status_code=status.HTTP_200_OK)
async def send_message(msg : Message):
    """    
    :param msg: Description
    :type msg: Message
    :return: Description
    :rtype: dict[str, Any]"""
    
    resposne = await produce(msg)
    return resposne


# Add the background task for the consumer
def add_kafka_consumer(app: FastAPI):
    """    
    :param app: Description
    :type app: FastAPI"""
    @app.on_event("startup")
    async def startup_event():
        """
        Start the Kafka consumer when the FastAPI app starts.
        """
        asyncio.create_task(consume())