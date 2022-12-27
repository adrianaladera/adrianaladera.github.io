from flask import Flask, render_template
  
app = Flask(__name__)
  
# Pass the required route to the decorator.
@app.route('/')
def index():
    return render_template('home.html')

@app.route("/research")
def research():
    return render_template("research.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/play")
def play():
    return render_template("play.html")

@app.route("/other-sites")
def other_sites():
    return render_template("sites.html")

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
    
if __name__ == "__main__":
    app.run()