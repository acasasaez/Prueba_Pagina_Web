from flask import Flask 
app = Flask(__name__)

@app.route("/")
def principal(): 
    return "Hola, soy Andrea"

if __name__ == "__main__":
    app.run( debug =True, port = 3000 )