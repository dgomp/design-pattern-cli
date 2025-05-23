from flask import Flask, request, jsonify
from pattern_recommender import PatternRecommender

app = Flask(__name__)

recommender = PatternRecommender()

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        if not data or 'useCase' not in data:
            return jsonify({'error': 'Caso de uso não fornecido'}), 400
        use_case = data['useCase']
        recommendation = recommender.analyze_use_case(use_case)
        return jsonify(recommendation)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 