from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route('/application-form')
def show_application_form():
    """Show form for job application."""

    return render_template("application-form.html")


@app.route('/application', methods=["POST"])
def application_form():
    """Handle the submission of a job application form"""

    first = request.form.get("firstname")
    last = request.form.get("lastname")
    pay = request.form.get("salary")
    jobtitle = request.form.get("jobtype")

    return render_template("application-response.html",
                           firstname=first,
                           lastname=last,
                           salary=pay,
                           jobtype=jobtitle,
                           )


if __name__ == "__main__":
    app.run(debug=True)
