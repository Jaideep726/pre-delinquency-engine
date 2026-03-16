import pandas as pd
from sqlalchemy import create_engine

print("Connecting to PostgreSQL database...")
# This connects to the Docker container you just built
engine = create_engine('postgresql://admin:password123@localhost:5432/banking_db')

print("Reading CSV files...")
df_customers = pd.read_csv('data/customers.csv')
df_transactions = pd.read_csv('data/transactions.csv')

print("Loading customers into database...")
df_customers.to_sql('customers', engine, if_exists='replace', index=False)

print("Loading transactions into database...")
df_transactions.to_sql('transactions', engine, if_exists='replace', index=False)

print("Success! All historical data is securely loaded into PostgreSQL.")