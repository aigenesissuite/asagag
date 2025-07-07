from pinecone import Pinecone
import os

# Hardcode your key temporarily (we'll delete this file after)
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# List current indexes
indexes = pc.list_indexes()
print("Current indexes:", [idx.name for idx in indexes])

# Create our index
try:
    pc.create_index(
        name='genius-framework',
        dimension=1536,
        metric='cosine',
        spec={'serverless': {'cloud': 'aws', 'region': 'us-east-1'}}
    )
    print("✅ Index 'genius-framework' created!")
except Exception as e:
    print(f"Error: {e}")
