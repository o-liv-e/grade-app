from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    marks = data.get('marks', [])
    
    if not marks:
        return jsonify({"error": "No marks provided"}), 400
        
    total = sum(marks)
    average = total / len(marks)
    
    return jsonify({
        "total": total,
        "average": average
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
