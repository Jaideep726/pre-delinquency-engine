from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, String

# 1. Define the Customer Entity
customer = Entity(
    name="customer", 
    join_keys=["customer_id"], 
    description="Customer identifier for risk scoring"
)

# 2. Point Feast to our new Parquet file
transaction_source = FileSource(
    path="../data/transactions.parquet",
    timestamp_field="timestamp"
)

# 3. Define the Feature View
customer_risk_features = FeatureView(
    name="customer_risk_features",
    entities=[customer],
    ttl=timedelta(days=90),
    schema=[
        Field(name="amount", dtype=Float32),
        Field(name="category", dtype=String),
    ],
    online=True,
    source=transaction_source,
    tags={"team": "risk_analytics"},
)