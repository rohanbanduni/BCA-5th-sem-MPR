from flask import Flask, render_template, request
#import your_ml_model  # Import your machine learning model module

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user inputs from the form
        high_bp = int(request.form['HighBP'])
        high_chol = int(request.form['HighChol'])
        bmi = float(request.form['BMI'])
        gen_hlth = int(request.form['GenHlth'])
        ment_hlth = int(request.form['MentHlth'])
        phys_hlth = int(request.form['PhysHlth'])
        diff_walk = int(request.form['DiffWalk'])
        age = int(request.form['Age'])
        income = int(request.form['Income'])
        physical_hlth = int(request.form['PhysicalHlth'])

        # Call your machine learning model to make a prediction
     #   prediction = your_ml_model.predict([[high_bp, high_chol, bmi, gen_hlth, ment_hlth, phys_hlth, diff_walk, age, income, physical_hlth]])
        # Modify this line based on your model's input format

        # Return the prediction to the user
    #    return render_template('predict.html', prediction=prediction[0])
        # Modify this line based on your result rendering

if __name__ == '__main__':
    app.run(debug=True)
