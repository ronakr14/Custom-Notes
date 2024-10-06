# AMQPStorm Module in Python: A Comprehensive Guide

AMQPStorm is a lightweight, fast, and highly optimized library for working with AMQP (Advanced Message Queuing Protocol) in Python. This guide will cover the key features, functionalities, and provide detailed examples to help you get started with AMQPStorm.

## Introduction to AMQPStorm

AMQPStorm is designed to be a flexible and easy-to-use library for interfacing with AMQP brokers like RabbitMQ. It provides high-level methods for connecting, publishing, consuming, and managing AMQP resources.

Key features of AMQPStorm:
- Easy to use and lightweight
- Supports synchronous and asynchronous operations
- High-level API for common AMQP tasks
- Connection and channel management
- Supports AMQP 0.9.1

## Installation

To install AMQPStorm, you can use pip:

```bash
pip install amqpstorm
```

## Connecting to an AMQP Broker

To connect to an AMQP broker, you need the broker's URL or the individual connection parameters.

```python
from amqpstorm import UriConnection

# Connect to the broker using URI
connection = UriConnection('amqp://guest:guest@localhost:5672/%2F')

# Alternatively, use Connection class
from amqpstorm import Connection

connection = Connection('localhost', 'guest', 'guest')
```

## Publishing Messages

Publishing messages to an exchange is straightforward with AMQPStorm.

```python
from amqpstorm import Connection

# Establish connection
connection = Connection('localhost', 'guest', 'guest')
channel = connection.channel()

# Declare the exchange
channel.exchange.declare(exchange='example_exchange', exchange_type='direct')

# Publish message
channel.basic.publish(body='Hello, World!', routing_key='example_key', exchange='example_exchange')

# Close the connection
channel.close()
connection.close()
```

## Consuming Messages

Consuming messages from a queue involves setting up a consumer and processing messages in a callback function.

```python
from amqpstorm import Connection

def message_callback(message):
    print("Received message:", message.body)
    message.ack()

# Establish connection
connection = Connection('localhost', 'guest', 'guest')
channel = connection.channel()

# Declare the queue
channel.queue.declare('example_queue')

# Bind the queue to an exchange
channel.queue.bind(queue='example_queue', exchange='example_exchange', routing_key='example_key')

# Start consuming
channel.basic.consume(queue='example_queue', callback=message_callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.close()
    connection.close()
```

## Queues

Declaring and managing queues in AMQPStorm.

```python
# Declare a queue
channel.queue.declare('example_queue', durable=True)

# Bind queue to an exchange
channel.queue.bind(queue='example_queue', exchange='example_exchange', routing_key='example_key')

# Delete a queue
channel.queue.delete('example_queue')
```

## Exchanges

Declaring and managing exchanges in AMQPStorm.

```python
# Declare an exchange
channel.exchange.declare(exchange='example_exchange', exchange_type='direct', durable=True)

# Delete an exchange
channel.exchange.delete('example_exchange')
```

## Message Acknowledgment

AMQPStorm supports manual acknowledgment of messages.

```python
def message_callback(message):
    print("Received message:", message.body)
    message.ack()

# Start consuming with acknowledgment
channel.basic.consume(queue='example_queue', callback=message_callback)
channel.start_consuming()
```

## Error Handling

AMQPStorm provides mechanisms to handle errors gracefully.

```python
from amqpstorm import AMQPError

try:
    connection = Connection('localhost', 'guest', 'guest')
    channel = connection.channel()
    channel.basic.publish(body='Hello, World!', routing_key='example_key', exchange='example_exchange')
except AMQPError as e:
    print("An error occurred:", e)
finally:
    channel.close()
    connection.close()
```

## Advanced Features

### Publisher Confirms

Publisher confirms ensure that messages have been successfully published.

```python
channel.confirm_deliveries()

try:
    channel.basic.publish(body='Hello, World!', routing_key='example_key', exchange='example_exchange')
    print("Message published successfully")
except AMQPError:
    print("Failed to publish message")
```

### Message Properties

Setting message properties like headers, content type, and delivery mode.

```python
from amqpstorm import Message

message = Message.create(channel, body='Hello, World!', properties={
    'content_type': 'text/plain',
    'delivery_mode': 2  # Persistent
})

message.publish(routing_key='example_key', exchange='example_exchange')
```

### RPC (Remote Procedure Call)

Implementing RPC with AMQPStorm.

```python
import uuid

def on_response(message):
    print("Received response:", message.body)
    message.ack()

# Declare a callback queue
result = channel.queue.declare('', exclusive=True)
callback_queue = result['queue']

# Publish the RPC request
correlation_id = str(uuid.uuid4())
channel.basic.publish(body='RPC Request', routing_key='rpc_queue', properties={
    'reply_to': callback_queue,
    'correlation_id': correlation_id
})

# Consume the response
channel.basic.consume(callback_queue, on_response)
channel.start_consuming()
```

## Conclusion

AMQPStorm is a robust and efficient library for working with AMQP brokers like RabbitMQ. Its high-level API simplifies the process of connecting, publishing, consuming, and managing AMQP resources. By mastering the core features and functionalities of AMQPStorm, you can create powerful and reliable messaging systems with minimal effort.