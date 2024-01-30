from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure secret key


@app.route('/')
def home_page():
    return render_template('index.html')


class CaloriesForm(FlaskForm):
    weight = StringField("Weight (kg):")
    height = StringField("Height (cm):")
    age = StringField("Age:")
    city = StringField("City:")
    country = StringField("Country:")
    button = SubmitField("Calculate")


@app.route('/calories_form', methods=["GET", "POST"])
def calories_form_page():
    result = False
    calories_form = CaloriesForm()
    if request.method == "GET":
        return render_template('calories_form_page.html', caloriesform=calories_form, result=result)
    elif request.method == "POST":
        form_data = request.form.copy()  # Returns data as JSON/dictionary
        form_temperature = int(Temperature(form_data['country'].lower().replace(" ", "-"),
                                           form_data['city'].lower().replace(" ", "-")).get_value())
        result = Calorie(int(form_data['weight']),
                         int(form_data['height']),
                         int(form_data['age']),
                         form_temperature).calculate()
        return render_template('calories_form_page.html', caloriesform=calories_form, result=result)


if __name__ == "__main__":
    app.run()
