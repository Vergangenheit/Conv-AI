from flask import Flask, render_template, request, url_for
from app.forms import ReusableForm
from app.generate import generate_from_seed
import json

# instantiate app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# create homepage
@app.route("/get_response", methods=["POST"])
def home():
    try:
        input_text = ' '.join(request.json['input_text'].split())
        out_text = generate_from_seed(args=args, personality=personality, db=db, seed=input_text)
        return app.response_class(json.dumps(out_text), status=200, mimetype='application/json')

    except Exception as e:
        err = str(e)
        print(err)
        return app.response_class(response=json.dumps(err), status=500, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug=True)