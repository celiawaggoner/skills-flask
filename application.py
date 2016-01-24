from flask import Flask, render_template, request

app = Flask(__name__)

#local host home page
@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

#show the application form HTML on this page
@app.route("/application-form")
def show_form():
    """Shows application form"""

    return render_template("application-form.html")

#get responses from form, format them with Jinja and return a response
@app.route("/application", methods=["POST"])
def submit_form():
    """Submit application form"""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    job_title = request.form.get("jobtitle")

    return render_template("application-responses.html",
                            first_name=first_name,
                            last_name=last_name,
                            salary=salary,
                            job_title=job_title)


if __name__ == "__main__":
    app.run(debug=True)
