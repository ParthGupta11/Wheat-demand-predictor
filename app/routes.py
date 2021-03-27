from app import app
from flask import render_template, redirect, url_for, request
import pickle
import numpy as np

file = open("svr_model.pkl", "rb")
regressor = pickle.load(file)


@app.route('/', methods=["GET"])	
def home():
	return render_template("index.html")


@app.route("/prediction", methods=["POST"])
def prediction():
	if request.method == "POST":
		year = int(request.form["year"])
		year = (year - 1989.3958)/17.503
		population = int(request.form["population"])
		population = (population - 877977753)/290867828.935
		wheat_surplus = float(request.form["wheat_surplus"])
		wheat_surplus = (wheat_surplus + 0.617)/4.6084
		final_features = np.array([[year, population, wheat_surplus]])
		demand = regressor.predict(final_features)
		demand = (demand * 26.1050) + 52.10958
		return render_template("index.html", 
			                    prediction_text = "The market demand is {:0.3f} million metric tonnes".format(demand[0]), 
			                    year  = int(request.form["year"]), 
			                    population = int(request.form["population"]),
			                    wheat_surplus = float(request.form["wheat_surplus"]))

	else:
		return render_template("index.html")