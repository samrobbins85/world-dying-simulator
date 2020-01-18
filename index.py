from flask import Flask, Response, request, render_template
import sys
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    sea_level = request.args.get('sea_level')
    temperature = request.args.get('temperature')
    fire = request.args.get('fire')
    if sea_level == None:
        sea_level = 300
    print(temperature)
    if temperature=="hot":
        temperature="https://world-dying.now.sh/person/hot.png"
        print(temperature)
    else:
        temperature="https://world-dying.now.sh/person/cold.png"


    return render_template('test.html', sea_level=sea_level, temperature=temperature, fire=fire)
 
