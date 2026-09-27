from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        
       
        url = f"https://wttr.in/{city}?format=j1"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                
                current = data['current_condition'][0]
                weather_data = {
                    'city': city.capitalize(),
                    'temp': current['temp_C'],
                    'description': current['weatherDesc'][0]['value'],
                    'humidity': current['humidity'],
                    'wind': current['windspeedKmph']
                }
            else:
                error = "Could not find weather data for that city."
        except Exception as e:
            error = "An error occurred while connecting to the weather service."
        
    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)