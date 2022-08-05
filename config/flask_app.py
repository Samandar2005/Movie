from flask_app import app
import sys
path = '/home/samandar02/config'
if path not in sys.path:
    sys.path.insert(0, path)
app.run(host='127.0.0.1', port=8000, debug=True)
