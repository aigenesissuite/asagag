from flask import Flask, request, jsonify
from flask_cors import CORS
from vector_store import GeniusVectorStore
import os

app = Flask(__name__)
CORS(app)  # Allow Typebot to call this

# Initialize store
store = GeniusVectorStore()

@app.route('/genius', methods=['POST'])
def query_genius():
    """Endpoint for Typebot to get relevant patterns"""
    try:
        data = request.json

        # Get parameters from Typebot
        query_text = data.get('query', '')
        companion_type = data.get('companion', 'email')
        client_name = data.get('client', 'RTR')
        customer_segment = data.get('segment', 'general')

        # Build smart query
        enhanced_query = f"{companion_type} {query_text}"

        # Set filters based on companion type
        filters = {'client': client_name}
        if companion_type == 'email':
            filters['type'] = 'email_subject'

        # Get relevant patterns
        patterns = store.find_patterns(enhanced_query, filters, count=3)

        # Get framework patterns too
        framework_patterns = store.find_patterns(query_text, {'framework': 'trojan'}, count=2)

        # Format response for Typebot
        examples = [p['text'] for p in patterns if p['score'] > 0.2]
        framework_rules = [p['text'] for p in framework_patterns if p['score'] > 0.2]

        return jsonify({
            'success': True,
            'examples': examples,
            'framework': framework_rules,
            'prompt_enhancement': f"Optimized for {customer_segment} customers"
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'examples': ["Use RTR's confident, friendly voice"],
            'framework': ["Create urgency naturally"]
        })

@app.route('/genius/vector-search', methods=['POST'])
def vector_search():
    """Vector search endpoint for Typebot companions"""
    try:
        data = request.json
        
        # Get query and filter from request
        query = data.get('query', '')
        filter_params = data.get('filter', {})
        top_k = data.get('top_k', 5)
        
        # Search the vector store
        results = store.find_patterns(query, filter_params, count=top_k)
        
        # Format results for display
        formatted_results = []
        for result in results:
            if result['score'] > 0.2:  # Only include relevant results
                formatted_results.append(f"• {result['text']} (relevance: {result['score']:.2f})")
        
        # Return formatted string for direct use in prompts
        return '\n'.join(formatted_results) if formatted_results else "No specific patterns found - using general best practices."
        
    except Exception as e:
        print(f"Vector search error: {str(e)}")
        return "Error retrieving patterns - using default approach."

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'genius-framework'})

if __name__ == '__main__':
    print("🚀 Starting Genius Framework API...")
    print("📡 API available at: http://localhost:5001") 
    print("🔌 Webhook URL for Typebot: http://localhost:5001/genius")
    print("🔌 Vector Search URL: http://localhost:5001/genius/vector-search")
    app.run(debug=True, port=5001)
