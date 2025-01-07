from flask import Flask, render_template, request, redirect, url_for
import pickle


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')
    




with open("classifier_loan.pkl", "rb") as file:
    clf = pickle.load(file)


#this will be my result checker html page
@app.route("/submit", methods=["POST"])
def submit_form():
    total_score = 0
    if request.method == "POST":
        
        gender = request.form.get("gender")
        if gender == "Male":
            gender = 0
        else:
            gender = 1
        print(gender, flush=True)
        

        married = request.form.get("married")
        if married == "Yes":
            married = 1
        else:
            married = 0
        print(married, flush=True)
        '''
        gender1 = float(request.form["gender"])
        print(gender1, flush=True)
        married1 = float(request.form["married"])
        print(married1, flush=True)
        applicant_income1 = float(request.form["applicant_income"])
        print(applicant_income1, flush=True)
        loan_amount1 = float(request.form["loan_amount"])
        print(loan_amount1, flush=True)
        credit_history1 = float(request.form["credit_history"])
        print(credit_history1, flush=True)
        '''
        #'''
        #gender = int(request.form.get("gender", 0))
        #print(gender, flush=True)
        #married = int(request.form.get("married", 0))
        #print(married, flush=True)
        applicant_income = int(request.form.get("applicant_income", 0))
        print(applicant_income, flush=True)
        loan_amount = int(request.form.get("loan_amount", 0))
        print(loan_amount, flush=True)
        credit_history = int(request.form.get("credit_history", 0))
        print(credit_history, flush=True)
        #'''

        input_data = [gender, married, applicant_income, loan_amount, credit_history]

        result = clf.predict([input_data])

        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        
        cont = {
        "pred" : pred, 
        "gender" : gender, 
        "married" : married,
        "applicant_income" : applicant_income, 
        "loan_amount" : loan_amount, 
        "credit_history" : credit_history
        }

        return render_template("result.html", **cont)
        #return redirect(url_for('result1', **cont))
        #return redirect(url_for('result1', pred=pred, gender=gender, married=married, applicant_income=applicant_income, loan_amount=loan_amount,credit_history=credit_history))
        
'''
@app.route("/predict")
def result1(**cont):
    return render_template("result.html", **cont)    
'''


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    