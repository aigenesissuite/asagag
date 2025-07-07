from vector_store import GeniusVectorStore

def load_rtr_full_data():
    store = GeniusVectorStore()
    
    print("🏁 Loading complete RTR brand data...")
    
    # Brand voice and tone
    brand_data = {
        'tone': 'Confident, Professional, Friendly',
        'forbidden': 'Corporate buzzwords, trendy slang, profanity, bandwidth',
        'customer_values': 'Pride in vehicle, community, look/feel/design, performance, standing out',
        'transformation': 'Stand out amongst the crowd, confidence in daily life'
    }
    
    store.add_pattern(str(brand_data), {
        'client': 'RTR',
        'type': 'brand_profile',
        'category': 'voice'
    })
    
    # Email examples with rich metadata
    email_examples = [
        {
            'text': 'Subject: Get Up to $225 OFF Your Next Set Of Wheels!\nPreview: No codes - Just instant savings in your cart\nEyeing Your Next Set of Wheels? We Got You!',
            'metadata': {'client': 'RTR', 'type': 'email', 'performance': 'high', 'has_discount': True}
        },
        {
            'text': 'Subject: Celebrate James Deane\'s First 2025 FD Win! 🎉\nPreview: Save on RTR apparel and team gear today!\nJames Deane Takes The Win at FD Atlanta!',
            'metadata': {'client': 'RTR', 'type': 'email', 'category': 'racing', 'has_emoji': True}
        },
        {
            'text': 'Subject: These New Diecast Models are HOT! 🔥\nPreview: This exclusive release sold out in under an hour last week!\nRacing fans and collectors, this is your moment!',
            'metadata': {'client': 'RTR', 'type': 'email', 'creates_urgency': True, 'category': 'collectibles'}
        }
    ]
    
    for example in email_examples:
        store.add_pattern(example['text'], example['metadata'])
    
    # Key phrases and signatures
    signatures = [
        'Ready to Rock',
        'We Got You',
        'Don\'t miss out',
        'Act fast',
        'No codes needed',
        'Auto-applied at checkout',
        'Limited time offer',
        'Exclusive release'
    ]
    
    for sig in signatures:
        store.add_pattern(sig, {
            'client': 'RTR',
            'type': 'signature_phrase',
            'usage': 'brand_voice'
        })
    
    # Customer segment patterns
    segments = [
        {
            'text': 'DIY focused, cost-conscious, social media savvy, 18-45 years old',
            'metadata': {'client': 'RTR', 'type': 'customer_segment', 'segment': 'parts_customers'}
        },
        {
            'text': 'Affluent, business owners, want exclusive/turnkey solutions, 45-70+ years old',
            'metadata': {'client': 'RTR', 'type': 'customer_segment', 'segment': 'vehicle_customers'}
        }
    ]
    
    for segment in segments:
        store.add_pattern(segment['text'], segment['metadata'])
    
    print("✅ RTR brand data fully loaded!")
    
    # Test queries
    print("\n🔍 Testing enhanced queries...")
    
    test_queries = [
        ('discount email for wheels', {'client': 'RTR', 'has_discount': True}),
        ('racing victory announcement', {'client': 'RTR', 'category': 'racing'}),
        ('parts customer messaging', {'client': 'RTR', 'segment': 'parts_customers'})
    ]
    
    for query, filters in test_queries:
        print(f"\nQuery: {query}")
        results = store.find_patterns(query, filters, count=2)
        for r in results:
            print(f"  - {r['text'][:60]}... (score: {r['score']:.2f})")

if __name__ == "__main__":
    load_rtr_full_data()
