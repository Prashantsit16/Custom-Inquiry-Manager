from unicodedata import category

from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from models.inquiry import Inquiry
from services.bedrock_service import summarize_inquiry

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        ai_result = summarize_inquiry(message)

        new_inquiry = Inquiry(
            name=name,
            email=email,
            subject=subject,
            message=message,
            summary=ai_result["summary"],
            category=ai_result["category"],
            priority=ai_result["priority"],
            department=ai_result["department"],
            status="Pending"
        )

        db.session.add(new_inquiry)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    inquiries = Inquiry.query.all()

    total = Inquiry.query.count()

    pending = Inquiry.query.filter_by(status="Pending").count()

    resolved = Inquiry.query.filter_by(status="Resolved").count()

    high = Inquiry.query.filter_by(priority="High").count()

    return render_template(
        "dashboard.html",
        inquiries=inquiries,
        total=total,
        pending=pending,
        resolved=resolved,
        high=high
    )

@app.route("/inquiry/<int:id>")
def inquiry_detail(id):

    inquiry = Inquiry.query.get_or_404(id)

    return render_template(
        "details.html",
        inquiry=inquiry
    )
@app.route("/update_status/<int:id>", methods=["POST"])
def update_status(id):

    inquiry = Inquiry.query.get_or_404(id)

    inquiry.status = request.form["status"]

    db.session.commit()

    return redirect(url_for("inquiry_detail", id=id))

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)