import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def help():
    return "Orders not implemented"

@app.route('/healthz')
def health_check():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
