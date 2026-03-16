import pandas as pd
import json
import time
import random
from kafka import KafkaProducer
from datetime import datetime
import uuid

print("Connecting to Apache Kafka...")
# Connects to the Docker container running Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Loading customer roster...")
df_customers = pd.read_csv('data/customers.csv')
customer_ids = df_customers['customer_id'].tolist()

print("Starting LIVE transaction stream... (Press Ctrl+C to stop)")
topic_name = 'live_transactions'

try:
    while True:
        # Simulate a live card swipe
        cust_id = random.choice(customer_ids)
        transaction = {
            'transaction_id': str(uuid.uuid4()),
            'customer_id': cust_id,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'amount': round(random.uniform(5, 500), 2),
            'category': random.choice(['Groceries', 'Discretionary', 'Utility', 'Transport']),
            'type': 'Debit'
        }
        
        # Push the transaction into the Kafka stream
        producer.send(topic_name, transaction)
        print(f"🟢 STREAMING: Card swipe detected! User {cust_id[:8]}... spent ${transaction['amount']}")
        
        # Wait 1 to 2 seconds before the next person swipes their card
        time.sleep(random.uniform(0.5, 2.0))
        
except KeyboardInterrupt:
    print("\nStreaming stopped by user.")