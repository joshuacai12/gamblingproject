import os

from flask import Flask, flash, redirect, render_template, request, session

from helpers import apology

# Configure application.
app = Flask(__name__)

# Ensure templates are auto reloaded.
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    # this shows our introduction page of the website
    if request.method == "GET":
        return render_template("index.html")


@app.route("/questions", methods=["GET", "POST"])
def questions():


    # this checks if the user made input
    if request.method == "POST":

        # counter variable for rating
        person_data_number = 0

        # Assess question 1 and add to variable if necessary.
        answer1 = request.form['radio1']
        if answer1 == "true":
            person_data_number +=1
        else:
            person_data_number += 0

        # Assess question 2 and add to variable if necessary.
        answer2 = request.form['radio2']
        if answer2 == "true":
            person_data_number +=1
        else:
            person_data_number += 0

        # Assess question 3 and add to variable if necessary.
        answer3 = request.form['radio3']
        if answer3 == "true":
            person_data_number +=1
        else:
            person_data_number += 0

        # Assess question 4 and add to variable if necessary.
        answer4 = request.form['radio4']
        if answer4 == "true":
            person_data_number +=1
        else:
            person_data_number += 0

        # Assess question 5 and add to variable if necessary.
        answer5 = request.form['radio5']
        if answer5 == "true":
            person_data_number +=1
        else:
            person_data_number += 0

        # Assess question 6 and add to variable if necessary.
        answer6 = request.form['radio6']
        if answer6 == "true":
            person_data_number +=1
        else:
            person_data_number += 0

        # Assess question 7 and add to variable if necessary.
        answer7 = request.form['radio7']
        if answer7 == "true":
            person_data_number +=1
        else:
            person_data_number += 0

        # Assess question 8 and add to variable if necessary.
        answer8 = request.form['radio8']
        if answer8 == "true":
            person_data_number +=1
        else:
            person_data_number += 0

        # Assess question 9 and add to variable if necessary.
        answer9 = request.form['radio9']
        if answer9 == "true":
            person_data_number +=1
        else:
            person_data_number += 0



        # made a proportion based on the user's score
        proportion = person_data_number / 9

        # formatted it as a percentage for our our scale
        percent = "{:.0%}".format(proportion)

        rating = ""

        # Return different HTML pages based on the score received from the form. Returning these templates with user specific variables.
        if person_data_number == 0 :
            return render_template("low.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 1:
            return render_template("low.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 2:
            return render_template("low.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 3:
            return render_template("low.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 4:
            return render_template("medium.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 5:
            return render_template("medium.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 6:
            return render_template("medium.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 7:
            return render_template("high.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 8:
            return render_template("high.html", percent=percent, person_data_number=person_data_number)
        if person_data_number == 9:
            return render_template("high.html", percent=percent, person_data_number=person_data_number)

    else:
        return render_template("questions.html")


@app.route("/stats")
def stats():

    if request.method == "GET":

        return render_template("stats.html")

@app.route("/resources")
def resources():

    # directs user to the resources page of the website
    if request.method == "GET":

        return render_template("resources.html")













