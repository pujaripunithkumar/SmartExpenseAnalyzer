from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from datetime import date
import os

app = Flask(__name__)

if not os.path.exists("static"):
    os.mkdir("static")

if not os.path.exists("expenses.csv"):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
    df.to_csv("expenses.csv", index=False)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        category = request.form.get("category")
        amount = request.form.get("amount")
        note = request.form.get("note")

        df = pd.DataFrame([{
            "Date": date.today(),
            "Category": category,
            "Amount": float(amount),
            "Note": note
        }])
        df.to_csv("expenses.csv", mode="a", header=False, index=False)
        message = "Expense added"

    return render_template("index.html", message=message)

@app.route("/summary")
def summary():
    df = pd.read_csv("expenses.csv")
    total = df["Amount"].sum()
    data = df.groupby("Category")["Amount"].sum().to_dict()
    return render_template("summary.html", total=total, data=data)

@app.route("/chart")
def chart():
    df = pd.read_csv("expenses.csv")
    if not df.empty:
        df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
        plt.savefig("static/chart.png")
        plt.close()
    return render_template("chart.html")

@app.route("/advice")
def advice():
    df = pd.read_csv("expenses.csv")
    total = df["Amount"].sum()
    food = df[df["Category"] == "Food"]["Amount"].sum()
    msg = "Control food expenses" if food > 0.4 * total else "Good spending"
    return render_template("advice.html", msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))