from flask import Flask, Response, request, render_template
import sys
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    sea_level = request.args.get('sea_level')
    if sea_level == None:
        sea_level = 300

#     print(username, file=sys.stderr)
    return render_template('test.html', sea_level=sea_level)
 
