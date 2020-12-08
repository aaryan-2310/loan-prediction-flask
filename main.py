from flask import Flask, render_template, request, flash
from inflation import calculation 
import pandas as pd

df = pd.read_csv("data/inflation.csv")
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title="Home - Lending Rupee")

@app.route("/individual")
def individual():
    return render_template("individual.html", title="Individual Loan Approval Prediction - Lending Rupee")

@app.route("/joint")
def joint():
    return render_template("joint.html", title="Joint Loan Approval Prediction - Lending Rupee")

@app.route("/emi_calculator")
def emi_calculator():
    return render_template("emi.html", title="EMI Calculator - Lending Rupee")

@app.route("/inflation_calculator")
def inflation_calculator():
    return render_template("inflation.html", title="Inflation Calculator - Lending Rupee")
    

    


if __name__ == "__main__":
    app.run(debug=True)