
from flask import Flask 
  
app = Flask(__name__) 

@app.route("/hello") 
def hello(): 
    return "Hello"
    
@app.route("/") 
def index(): 
    return "home"
  
if __name__ == "__main__": 
    app.run() 
