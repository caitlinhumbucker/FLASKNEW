from flask import Flask
from datetime import datetime 

app=Flask(__name__)

@app.route("/")
def home():
   
    today=datetime.now().strftime("%Y-%m/%d %H:%M:%S")
    
    html=f"""  
        <h1>Welcome to my home page</h1>
        <p>Click the link below to navigate</p>
            <h1>Welcome to my clock </h1>
            <a href="/about"> Go to about page</a>
    """
    return html

@app.route("/about")
def about():
    html="""
        <h1>Welcome to my about page</h1>
        <p>I'm an epic coder</p>
    """

    return html
app.run(debug=True, port=5000)