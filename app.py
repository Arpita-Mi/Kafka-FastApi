from fastapi import FastAPI
app = FastAPI()
from src.routes.router import router
from src.api.v1.main.view import add_kafka_consumer


app.include_router(router)
add_kafka_consumer(app)