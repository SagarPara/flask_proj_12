from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')
    

with open("classifier_loan.pkl", "rb") as file:
    clf = pickle.load(file)


#this will be my result checker html page
@app.route("/submit", methods=["GET", "POST"])
def submit():
    total_score = 0
    if request.method == "POST":
        gender = request.form["gender"]
        if gender == "Male":
            Gender = 0
        else:
            Gender = 1

        married = request.form["married"]
        if married == "Yes":
            Married = 1
        else:
            Married = 0


        applicant_income = float(request.form["applicant_income"])
        loan_amount = float(request.form["loan_amount"])
        credit_history = float(request.form["credit_history"])
        
        input_data = [Gender, Married, applicant_income, loan_amount, credit_history]

        result = clf.predict([input_data])

        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        return render_template("result.html", result=pred, gender=Gender, married=Married, applicantincome=applicant_income, loanamount=loan_amount, credithistory=credit_history)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    