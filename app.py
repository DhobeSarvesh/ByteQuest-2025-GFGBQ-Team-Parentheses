from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

def calculate_return(amount, option):
    if option == "FD":
        return amount + amount * 0.05
    elif option == "Gold":
        return amount + amount * 0.07
    else:
        return amount + amount * 0.10

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        return redirect("/dashboard?user=" + username)
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect("/")
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    user = request.args.get("user")
    return render_template("dashboard.html", user=user)

@app.route("/invest", methods=["GET", "POST"])
def invest():
    if request.method == "POST":
        user = request.form["user"]
        option = request.form["option"]
        amount = int(request.form["amount"])

        result = calculate_return(amount, option)

        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([user, option, amount, result])

        return render_template("result.html", result=result)

    user = request.args.get("user")
    return render_template("invest.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
