from flask import Flask, render_template, request
import os
import joblib
import numpy as np
app = Flask(__name__)
model=joblib.load(open('model_joblib.joblib','rb'))

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/predict', methods=['POST'])
def home():

    data1 = request.form['Months_on_book']
    data2 = request.form['Total_Relationship_Count']
    data3 = request.form['Months_Inactive_12_mon']
    data4 = request.form['Contacts_Count_12_mon']
    data5 = request.form['Credit_Limit']
    data6 = request.form['Total_Revolving_Bal']
    data7 = request.form['Avg_Open_To_Buy']
    data8 = request.form['Total_Amt_Chng_Q4_Q1']
    data9 = request.form['Total_Trans_Amt']
    data10 = request.form['Total_Trans_Ct']
    data11 = request.form['Total_Ct_Chng_Q4_Q1']
    data12 = request.form['Avg_Utilization_Ratio']



    arr = np.array([[data1, data2, data3, data4,data5,data6,data7,data8,data9,data10,data11,data12]])
    pred = model.predict(arr)

    return render_template('result.html', Prediction='This client belong to group number:  {}'.format(pred[0]))
if __name__ == '__main__':

   app.run(host="0.0.0.0", debug=True,port=os.environ.get("PORT", 5000))
