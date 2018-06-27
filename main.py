from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello():
   time.sleep(3)
   return "blue"

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)
