from flask import Flask

from flask_cors import CORS


app = Flask(__name__)

CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!'







#Prueba
""" if __name__ == "__main__":

    app.run(debug=True) """

#Productivo
if __name__ == "__main__":

    serve(app, host='0.0.0.0',
            port=8080,
            threads=2      
            )