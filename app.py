from flask import Flask, jsonify
from datetime import datetime 
import calendar
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
currentDate = datetime.now()
    
@app.route('/monthData', methods= ['GET'])
def hundredKmPM():
    year = currentDate.year
    month = currentDate.month
    day = currentDate.day

    days = calendar.monthrange(year,month)[1]
    dayAverage = round(100 / days,2)  
    currentAverage = dayAverage * day
    
    return jsonify({
        'dayOfMonth': day,
        'monthDailyAverage': dayAverage,
        'monthCumulativeTarget': currentAverage
    })


@app.route('/yearData', methods=['GET'])
def thousandKmPY():
    currentDay = currentDate.timetuple().tm_yday
    currentAverage = round((1000/365)*currentDay, 1)

    return jsonify({
        'dayOfYear': currentDay,
        'yearlyCumulativeTarget': currentAverage
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)