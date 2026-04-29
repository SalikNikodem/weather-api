import os
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)


@app.route('/weather/<city>')
def get_weather(city):
    if not API_KEY:
        return jsonify({"error": "No API Key in .env"}), 500

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={API_KEY}&contentType=json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return jsonify(data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)