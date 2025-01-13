from flask import Flask, jsonify
from datetime import datetime 
import calendar
from flask_cors import CORS

app = Flask(__name__)
currentDate = datetime.now()

@app.route('/1000km', methods=['GET'])
def thousandKmPY():
    currentDay = currentDate.timetuple().tm_yday
    currentAverage = (1000/365)*currentDay

    return jsonify({
        'dayOfYear': currentDay,
        'yearlyCumulativeTarget': currentAverage
    })
    
@app.route('/100km', methods= ['GET'])
def hundredKmPM():
    year = currentDate.year
    month = currentDate.month
    day = currentDate.day

    days = calendar.monthrange(year,month)[1]
    dayAverage = 100 / days 
    currentAverage = dayAverage * day
    
    return jsonify({
        'dayOfMonth': day,
        'dailyAverage': dayAverage,
        'monthlyCumulativeTarget': currentAverage
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)