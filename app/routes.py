from flask import Flask, render_template, request, url_for
from app.forms import ReusableForm
from app.generate import generate_from_seed

# instantiate app
app = Flask(__name__)



# create homepage
@app.route("/", methods=["GET", "POST"])
def home():
    form = ReusableForm(request.form)
    if request.method == "POST" and form.validate():
        #extract info
        seed = request.form['seed']
        return render_template("seeded.html", input=generate_from_seed(args, model,
        tokenizer, personality, db, seed=seed))
        
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug=True)