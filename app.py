from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow requests from your frontend

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    
    # In a real application, you would process this data:
    # - Validate the data
    # - Send an email
    # - Save to a database
    print(f"Received message from {data['name']} ({data['email']}): {data['message']}")
    
    # For now, we'll just send a success response
    return jsonify({'message': 'Your message has been sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
