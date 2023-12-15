import pickle
import os
from flask import Flask, request, render_template

app = Flask(__name__)

base_path = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_path, 'pipe.pkl')

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        user_input = []
        features = [
            'HighBP', 'HighChol', 'BMI', 'GenHlth', 'DiffWalk', 'Age', 'Income'
        ]
        for feature in features:
            user_input.append((request.form.get(feature)))

        prediction = model.predict([user_input])
        return render_template('predict.html', prediction=prediction[0])

    return render_template('test.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')



if __name__ == '__main__':
    app.run(debug=True)
