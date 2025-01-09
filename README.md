## Kafka Producer and Consumer with FastAPI

This project demonstrates a basic Kafka producer-consumer integration with FastAPI. The producer sends messages to a Kafka topic, and the consumer listens to the messages from the topic asynchronously. The FastAPI application exposes an API endpoint to send messages to Kafka.

### Features

- **Producer**: Sends messages to a Kafka topic.
- **Consumer**: Listens to messages from the Kafka topic and processes them asynchronously.
- **FastAPI**: Exposes an API endpoint (`/send_message`) to send messages to Kafka.
- **Asynchronous**: Both the producer and consumer use asynchronous methods to avoid blocking the event loop.

### Prerequisites

- **Python 3.7+**
- **Kafka** (local or remote setup)
- **Apache ZooKeeper** (required for Kafka to run)
- **FastAPI and Uvicorn** for serving the API

#### Optional

- **Docker** (Docker Hub using the `apache/kafka` image)

### Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
   (After cloning, navigate to the project directory)

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Install Kafka for asynchronous operations:
    ```bash
    pip install aiokafka
    ```

### Usage

#### Starting the FastAPI Application

Run the FastAPI app using Uvicorn:
```bash
python run.py



**Sending a Message**
To send a message to Kafka, make a POST request to the /send_message endpoint with a JSON payload.

`Response` :
{
    "status": "Message sent",
    "topic": "test-topic",
    "partition": 0,
    "offset": 10,
    "key": null,
    "value": "Hello Kafka"
}

Kafka Consumer
The consumer listens to messages from the test-topic and processes them asynchronously. When a message is produced to Kafka, the consumer will print the message and related details to the console.