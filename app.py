from flask import Flask, render_template, request
from extensions import db
from models.inquiry import Inquiry

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        new_inquiry = Inquiry(
            name=request.form["name"],
            email=request.form["email"],
            subject=request.form["subject"],
            message=request.form["message"]
        )

        db.session.add(new_inquiry)
        db.session.commit()

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    inquiries = Inquiry.query.all()

    return render_template(
        "dashboard.html",
        inquiries=inquiries
    )


@app.route("/inquiry/<int:id>")
def inquiry_detail(id):

    inquiry = Inquiry.query.get_or_404(id)

    return render_template(
        "details.html",
        inquiry=inquiry
    )


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)