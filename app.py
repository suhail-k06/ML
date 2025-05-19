from flask import Flask,render_template,request
import pandas as pd
import joblib

app=Flask(__name__)

model=joblib.load('insurance_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    try:
        age=int(request.form['age'])
        sex=request.form['sex']
        bmi=float(request.form['bmi'])
        children=int(request.form['children'])
        smoker=request.form['smoker']
        region=request.form['region']
        n=pd.DataFrame({
             'age':[age],
             'sex':[sex],
             'bmi':[bmi],
             'children':[children],
             'smoker':[smoker],
             'region':[region]
        })
        print(n)
        prediction=model.predict(n)[0]
        print(prediction)
        return render_template('index.html',prediction_text=f'Insurance cost:₹{prediction:.2f}')
    except Exception as  e:
        return render_template('index.html',prediction_text=f"Error:{str(e)}")
if __name__=='__main__':
    app.run(debug=True)
    
