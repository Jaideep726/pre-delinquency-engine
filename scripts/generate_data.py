import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()
Faker.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 1000 
PERCENT_AT_RISK = 0.15
DAYS_OF_DATA = 90

print("Generating synthetic data...")

customers = []
for _ in range(NUM_CUSTOMERS):
    customers.append({
        'customer_id': fake.uuid4(),
        'age': random.randint(22, 65),
        'base_salary': round(random.uniform(3000, 12000), 2),
        'is_at_risk': random.random() < PERCENT_AT_RISK
    })

df_customers = pd.DataFrame(customers)

transactions = []
start_date = datetime.now() - timedelta(days=DAYS_OF_DATA)

for _, customer in df_customers.iterrows():
    cust_id = customer['customer_id']
    is_at_risk = customer['is_at_risk']
    salary = customer['base_salary']
    
    for month in range(3):
        current_month_date = start_date + timedelta(days=month*30)
        
        salary_lag = random.randint(3, 8) if is_at_risk else random.randint(0, 1)
        salary_date = current_month_date + timedelta(days=salary_lag)
        
        transactions.append({
            'transaction_id': fake.uuid4(),
            'customer_id': cust_id,
            'timestamp': salary_date.strftime('%Y-%m-%d %H:%M:%S'),
            'amount': salary,
            'category': 'Salary',
            'type': 'Credit'
        })
        
        num_discretionary = random.randint(1, 4) if is_at_risk else random.randint(5, 12)
        for _ in range(num_discretionary):
            transactions.append({
                'transaction_id': fake.uuid4(),
                'customer_id': cust_id,
                'timestamp': (current_month_date + timedelta(days=random.randint(2, 28))).strftime('%Y-%m-%d %H:%M:%S'),
                'amount': round(random.uniform(20, 150), 2),
                'category': 'Discretionary',
                'type': 'Debit'
            })
            
        utility_day = random.randint(25, 29) if is_at_risk else random.randint(5, 10)
        transactions.append({
            'transaction_id': fake.uuid4(),
            'customer_id': cust_id,
            'timestamp': (current_month_date + timedelta(days=utility_day)).strftime('%Y-%m-%d %H:%M:%S'),
            'amount': round(random.uniform(100, 300), 2),
            'category': 'Utility',
            'type': 'Debit'
        })

df_transactions = pd.DataFrame(transactions)

os.makedirs('data', exist_ok=True)
df_customers.to_csv('data/customers.csv', index=False)
df_transactions.to_csv('data/transactions.csv', index=False)

print(f"Success! Generated {len(df_customers)} customers and {len(df_transactions)} transactions.")