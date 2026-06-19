from flask import Flask, render_template, request
import joblib

model = joblib.load(r"C:\Users\Jaishree\OneDrive\Desktop\Flask\proiject\Loan\loan_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("predict.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    prediction = None

    if request.method == "POST":

        income = float(request.form['income'])
        credit_score = float(request.form['credit_score'])
        loan_amount = float(request.form['loan_amount'])
        years_employed = float(request.form['years_employed'])
        points = float(request.form['points'])

        pred = model.predict([[
            income,
            credit_score,
            loan_amount,
            years_employed,
            points
        ]])[0]

        if pred == 1:
            prediction = "✅ Loan Approved"
        else:
            prediction = "❌ Loan Rejected"

    return render_template(
        "predict.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)