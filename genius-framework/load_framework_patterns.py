from vector_store import GeniusVectorStore

def load_framework_patterns():
    store = GeniusVectorStore()
    
    print("🧠 Loading advanced framework patterns...")
    
    # RIFT patterns
    rift_patterns = [
        {
            'text': 'Your current setup is already outdated',
            'metadata': {'framework': 'rift', 'axis': 'breach', 'type': 'pattern'}
        },
        {
            'text': 'The pros already made this switch',
            'metadata': {'framework': 'rift', 'axis': 'insider', 'type': 'pattern'}
        },
        {
            'text': 'This becomes standard in 2026',
            'metadata': {'framework': 'rift', 'axis': 'future', 'type': 'pattern'}
        },
        {
            'text': 'You are not who you think you are',
            'metadata': {'framework': 'rift', 'axis': 'identity', 'type': 'pattern'}
        }
    ]
    
    # Hook patterns
    hook_patterns = [
        {
            'text': 'Still running stock? >>>',
            'metadata': {'framework': 'hook', 'type': 'caption', 'industry': 'automotive'}
        },
        {
            'text': 'What Ford won\'t tell you >>>',
            'metadata': {'framework': 'hook', 'type': 'caption', 'industry': 'automotive'}
        },
        {
            'text': 'Why do all Mustangs look the same?',
            'metadata': {'framework': 'hook', 'type': 'question', 'industry': 'automotive'}
        }
    ]
    
    for pattern in rift_patterns + hook_patterns:
        store.add_pattern(pattern['text'], pattern['metadata'])
    
    print("✅ Framework patterns loaded!")

if __name__ == "__main__":
    load_framework_patterns()
