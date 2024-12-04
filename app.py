# app.py
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the student information page
@app.route('/student')
def student():
    return render_template('student.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
