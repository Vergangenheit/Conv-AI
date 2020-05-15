from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request, url_for
from app.forms import ReusableForm
from app.generate import generate_from_seed

# instiate app
app = Flask(__name__)
#run_with_ngrok(app)

# create homepage
@app.route("/", methods=["GET", "POST"])
def home():
    form = ReusableForm(request.form)
    if request.method == "POST":
        return render_template("seeded.html", input=generate_from_seed(model=model, 
        tokenizer=tokenizer, personality=personality, seed=seed))
        
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug=True)
    #app.run()
