from flask import Flask, Response, request
import sys
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    username = request.args.get('username')
    print(username, file=sys.stderr)
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (username), mimetype="text/html")
 
