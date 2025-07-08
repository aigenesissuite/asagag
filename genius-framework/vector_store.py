import os 
import openai
from pinecone import Pinecone
from typing import Dict, List
import json
from dotenv import load_dotenv
            
# Load environment
load_dotenv()
     
# Initialize
openai.api_key = os.getenv('OPENAI_API_KEY')
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

class GeniusVectorStore:
    def __init__(self):
        self.index = pc.Index('genius-framework')
        print("✅ Connected to Genius Framework Vector Store")
    
    def embed_text(self, text: str) -> List[float]:
        """Create embedding using OpenAI"""
        response = openai.Embedding.create(
            model="text-embedding-ada-002",  # Changed to older model
            input=text
        )
        return response['data'][0]['embedding']
    
    def add_pattern(self, text: str, metadata: Dict):
        """Add any pattern to vector store"""
        vector_id = f"{metadata.get('client', 'universal')}_{metadata.get('type', 'general')}_{abs(hash(text))}"
        embedding = self.embed_text(text)
        metadata['text'] = text
        
        self.index.upsert([(vector_id, embedding, metadata)])
        print(f"✓ Added: [{metadata.get('type', 'general')}] {text[:50]}...")
    
    def find_patterns(self, query: str, filters: Dict = {}, count: int = 3):
        """Find relevant patterns for any client"""
        query_embedding = self.embed_text(query)
        
        results = self.index.query(
            vector=query_embedding,
            top_k=count,
            filter=filters,
            include_metadata=True
        )
        
        patterns = []
        for match in results['matches']:
            patterns.append({
                'text': match['metadata'].get('text', ''),
                'score': match['score'],
                'metadata': match['metadata']
            })
        
        return patterns

# Test the system
def test_framework():
    """Test the framework is working"""
    store = GeniusVectorStore()
    
    # Add some universal framework patterns
    print("\n🧠 Adding Universal Framework Patterns...")
    
    # TROJAN framework (works for any client)
    framework_patterns = [
        {
            'text': 'Expose the hidden cost or risk they are ignoring',
            'metadata': {'framework': 'trojan', 'driver': 'threat', 'type': 'pattern'}
        },
        {
            'text': 'Reference what the leaders in their space already do',
            'metadata': {'framework': 'trojan', 'driver': 'authority', 'type': 'pattern'}
        }, 
        {
            'text': 'Create urgency by showing the window is closing',
            'metadata': {'framework': 'trojan', 'driver': 'no_escape', 'type': 'pattern'}
        }
    ]

    for pattern in framework_patterns:
        store.add_pattern(pattern['text'], pattern['metadata'])
 
    print("\n✅ Framework ready for any client!")
    
    # Test query
    print("\n🔍 Testing universal query...")
    results = store.find_patterns("how to create urgency", {'framework': 'trojan'})
    
    for r in results:
        print(f"- {r['text'][:60]}... (score: {r['score']:.2f})")
            
if __name__ == "__main__":
    test_framework()
