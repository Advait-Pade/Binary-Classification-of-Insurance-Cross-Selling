import pandas as pd
from flask import Flask,render_template,request,jsonify
from codes.classify_customer import classify_customer

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/insurance_classifier', methods=['POST'])
def insurance_classifier():
    if request.method == 'POST':
        # Access the form values using request.form
        id = request.form.get('id')
        gender = request.form.get('gender')
        age = int(request.form.get('age'))  # Convert to integer
        driving_license = int(request.form.get('driving_license'))
        region_code = int(request.form.get('region_code'))  # Convert to integer
        previously_insured = int(request.form.get('previously_insured'))
        vehicle_age = request.form.get('vehicle_age')
        vehicle_damage = int(request.form.get('vehicle_damage'))
        annual_premium = float(request.form.get('annual_premium'))  # Convert to float
        policy_sales_channel = int(request.form.get('policy_sales_channel'))  # Convert to integer
        vintage = int(request.form.get('vintage'))  # Convert to integer
        
        column_names = ['id','Gender','Age','Driving_License','Region_Code','Previously_Insured','Vehicle_Age','Vehicle_Damage','Annual_Premium','Policy_Sales_Channel','Vintage']
        df = pd.DataFrame([[id, gender, age, driving_license, region_code, previously_insured, vehicle_age, vehicle_damage,annual_premium, policy_sales_channel, vintage]],columns = column_names)
        classification_result = classify_customer(df)

        # return classification_result
        return render_template('result.html', classification_result=classification_result)
    else:
        return "Invalid request method"

@app.route('/insurance_classifier_api', methods=['POST'])
def insurance_classifier_api():
    if request.method == 'POST':
        # Access the form values using request.form
        id = int(request.form.get('id'))
        gender = request.form.get('gender')
        age = int(request.form.get('age'))  # Convert to integer
        driving_license = int(request.form.get('driving_license'))
        region_code = int(request.form.get('region_code'))  # Convert to integer
        previously_insured = int(request.form.get('previously_insured'))
        vehicle_age = request.form.get('vehicle_age')
        vehicle_damage = int(request.form.get('vehicle_damage'))
        annual_premium = float(request.form.get('annual_premium'))  # Convert to float
        policy_sales_channel = int(request.form.get('policy_sales_channel'))  # Convert to integer
        vintage = int(request.form.get('vintage'))  # Convert to integer

        column_names = ['id','Gender','Age','Driving_License','Region_Code','Previously_Insured','Vehicle_Age','Vehicle_Damage','Annual_Premium','Policy_Sales_Channel','Vintage']
        df = pd.DataFrame([[id, gender, age, driving_license, region_code, previously_insured, vehicle_age, vehicle_damage,annual_premium, policy_sales_channel, vintage]],columns = column_names)
        classification_result = classify_customer(df)

         # Convert the result to a JSON response
        return jsonify({'classification_result': classification_result})
    else:
        return "Invalid request method", 400

if __name__ == '__main__':
    app.run(debug=True)