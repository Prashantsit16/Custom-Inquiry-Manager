from flask import Flask, render_template, request

app = Flask(__name__)

inquiries = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        inquiry = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }

        inquiries.append(inquiry)

        print(inquiries)

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",
        inquiries=inquiries
    )

@app.route("/inquiry/<int:index>")
def inquiry_detail(index):
    print(inquiries)
    inquiry = inquiries[index]
    

    return render_template(
        "details.html",
        inquiry=inquiry
    )
if __name__ == "__main__":
    app.run(debug=True)