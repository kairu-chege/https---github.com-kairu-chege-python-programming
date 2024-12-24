from flask import Flask, jsonify, request
import requests
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gaksduqwihi382rh4fn2022rh472gr' 
csrf = CSRFProtect(app) 

# ... other parts of your code ...

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Missing required parameter: city'}), 400  # Handle missing city parameter

    api_key = '8d2be4058f8f3cb911a362a2b44503e8'  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Error fetching weather data'}), response.status_code  # Handle API errors

if __name__ == '__main__':
    app.run(debug=True)