from flask import Flask, render_template, request

# instiate app
app = Flask(__name__)


# create homepage
@app.route("/", methods=["GET", "POST"])
def home():
    #return '<h1>Welcome to the chatbot interaction page</h1>'
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug=True)
