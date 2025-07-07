from vector_store import GeniusVectorStore
import pandas as pd

def process_rtr_data():
    store = GeniusVectorStore()
    
    print("🏁 Adding RTR-specific patterns...")
    
    # RTR's key phrases
    rtr_patterns = [
        {'text': 'Ready to Rock', 'metadata': {'client': 'RTR', 'type': 'phrase', 'usage': 'signature'}},
        {'text': 'We Got You', 'metadata': {'client': 'RTR', 'type': 'phrase', 'usage': 'support'}},
        {'text': "won't last long", 'metadata': {'client': 'RTR', 'type': 'phrase', 'usage': 'urgency'}},
        {'text': 'Get Up to $225 OFF Your Next Set Of Wheels!', 'metadata': {'client': 'RTR', 'type': 'email_subject'}},
        {'text': 'These New Diecast Models are HOT! 🔥', 'metadata': {'client': 'RTR', 'type': 'email_subject'}}
    ]
    
    for pattern in rtr_patterns:
        store.add_pattern(pattern['text'], pattern['metadata'])
    
    print("\n✅ RTR patterns added!")
    
    # Test RTR query
    print("\n🔍 Testing RTR query...")
    results = store.find_patterns("email subject for wheels", {'client': 'RTR'})
    for r in results:
        print(f"- {r['text']}")

if __name__ == "__main__":
    process_rtr_data()
