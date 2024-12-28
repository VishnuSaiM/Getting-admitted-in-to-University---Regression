import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

flask_app = Flask(__name__)
import pickle

model_path = "c:/Users/muppa/Downloads/Probability of Getting Admission/template/lrmodel.pkl"
model = pickle.load(open(model_path, "rb"))



@flask_app.route("/")
def Home():
    return render_template("index.html")
@flask_app.route("/predict",methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html",prediction_text = "The Chance of Getting admitted is {}.format(prediction) ")
if __name__ == "__main__":
    flask_app.run(debug=True)


