
from distutils.log import debug
from unicodedata import name
from flask import Flask, redirect,render_template,request
import numpy as np
import pickle
# from model import make_predictions

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])
def predict():
    if (request.method=='POST'):
        age=request.form['Age']
        print(age)
        DailyRate=request.form['DailyRate']
        DistanceFromHome=request.form['DistanceFromHome']
        EmployeeNumber=request.form['EmployeeNumber']
        HourlyRate=request.form['HourlyRate']
        MonthlyIncome=request.form['MonthlyIncome']
        MonthlyRate=request.form['MonthlyRate']
        NumCompaniesWorked=request.form['NumCompaniesWorked']
        PercentSalaryHike=request.form['PercentSalaryHike']
        TotalWorkingYears=request.form['TotalWorkingYears']
        TrainingTimesLastYear=request.form['TrainingTimesLastYear']
        YearsAtCompany=request.form['YearsAtCompany']
        YearsInCurrentRole=request.form['YearsInCurrentRole']
        YearsSinceLastPromotion=request.form['YearsSinceLastPromotion']
        YearsWithCurrManager=request.form['YearsWithCurrManager']
        BusinessTravel=request.form['BusinessTravel']
        if BusinessTravel=='0':
            BusinessTravel_Travel_Frequently='0'
            BusinessTravel_Travel_Rarely='0'
        elif BusinessTravel=='1':
            BusinessTravel_Travel_Frequently='0'
            BusinessTravel_Travel_Rarely='1'
        elif BusinessTravel=='2':
            BusinessTravel_Travel_Frequently='1'
            BusinessTravel_Travel_Rarely='0'
        else:
            pass

        JobInvolvement=request.form['JobInvolvement']
        if JobInvolvement=='0':
            JobInvolvement_2='0'
            JobInvolvement_3='0'
            JobInvolvement_4='0'
        elif JobInvolvement=='1':
            JobInvolvement_2='1'
            JobInvolvement_3='0'
            JobInvolvement_4='0'
        elif JobInvolvement=='2':
            JobInvolvement_2='0'
            JobInvolvement_3='1'
            JobInvolvement_4='0'
        elif JobInvolvement=='3':
            JobInvolvement_2='0'
            JobInvolvement_3='0'
            JobInvolvement_4='1'
        else:
            pass

        JobRole=request.form['JobRole']
        if JobRole=='0':
            JobRole_Human_Resources='0'
            JobRole_Laboratory_Technician='0'
            JobRole_Manager='0'
            JobRole_Manufacturing_Director='0'
            JobRole_Research_Director='0'
            JobRole_Research_Scientist='0'
            JobRole_Sales_Executive='0'
            JobRole_Sales_Representative='0'
        
        elif JobRole=='1':
            JobRole_Human_Resources='1'
            JobRole_Laboratory_Technician='0'
            JobRole_Manager='0'
            JobRole_Manufacturing_Director='0'
            JobRole_Research_Director='0'
            JobRole_Research_Scientist='0'
            JobRole_Sales_Executive='0'
            JobRole_Sales_Representative='0'
        elif JobRole=='2':
            JobRole_Human_Resources='0'
            JobRole_Laboratory_Technician='1'
            JobRole_Manager='0'
            JobRole_Manufacturing_Director='0'
            JobRole_Research_Director='0'
            JobRole_Research_Scientist='0'
            JobRole_Sales_Executive='0'
            JobRole_Sales_Representative='0'
        elif JobRole=='3':
            JobRole_Human_Resources='0'
            JobRole_Laboratory_Technician='0'
            JobRole_Manager='1'
            JobRole_Manufacturing_Director='0'
            JobRole_Research_Director='0'
            JobRole_Research_Scientist='0'
            JobRole_Sales_Executive='0'
            JobRole_Sales_Representative='0'
        elif JobRole=='4':
            JobRole_Human_Resources='0'
            JobRole_Laboratory_Technician='0'
            JobRole_Manager='0'
            JobRole_Manufacturing_Director='1'
            JobRole_Research_Director='0'
            JobRole_Research_Scientist='0'
            JobRole_Sales_Executive='0'
            JobRole_Sales_Representative='0'
        elif JobRole=='5':
            JobRole_Human_Resources='0'
            JobRole_Laboratory_Technician='0'
            JobRole_Manager='0'
            JobRole_Manufacturing_Director='0'
            JobRole_Research_Director='1'
            JobRole_Research_Scientist='0'
            JobRole_Sales_Executive='0'
            JobRole_Sales_Representative='0'
        elif JobRole=='6':
            JobRole_Human_Resources='0'
            JobRole_Laboratory_Technician='0'
            JobRole_Manager='0'
            JobRole_Manufacturing_Director='0'
            JobRole_Research_Director='0'
            JobRole_Research_Scientist='1'
            JobRole_Sales_Executive='0'
            JobRole_Sales_Representative='0'
        elif JobRole=='7':
            JobRole_Human_Resources='0'
            JobRole_Laboratory_Technician='0'
            JobRole_Manager='0'
            JobRole_Manufacturing_Director='0'
            JobRole_Research_Director='0'
            JobRole_Research_Scientist='0'
            JobRole_Sales_Executive='1'
            JobRole_Sales_Representative='0'
        elif JobRole=='8':
            JobRole_Human_Resources='0'
            JobRole_Laboratory_Technician='0'
            JobRole_Manager='0'
            JobRole_Manufacturing_Director='0'
            JobRole_Research_Director='0'
            JobRole_Research_Scientist='0'
            JobRole_Sales_Executive='0'
            JobRole_Sales_Representative='1'
        else:
            pass
        
        JobSatisfaction=request.form['JobSatisfaction']
        if JobSatisfaction=='0':
            JobSatisfaction_2='0'
            JobSatisfaction_3='0'
            JobSatisfaction_4='0'
        elif JobSatisfaction=='1':
            JobSatisfaction_2='1'
            JobSatisfaction_3='0'
            JobSatisfaction_4='0'
        elif JobSatisfaction=='2':
            JobSatisfaction_2='0'
            JobSatisfaction_3='1'
            JobSatisfaction_4='0'
        elif JobSatisfaction=='3':
            JobSatisfaction_2='0'
            JobSatisfaction_3='0'
            JobSatisfaction_4='1'
        else:
            pass

        MaritalStatus=request.form['MaritalStatus']
        if MaritalStatus=='0':
            MaritalStatus_Married='0'
            MaritalStatus_Single='0'
        elif MaritalStatus=='1':
            MaritalStatus_Married='1'
            MaritalStatus_Single='0'
        elif MaritalStatus=='2':
            MaritalStatus_Married='0'
            MaritalStatus_Single='0'
        else:
            pass

        OverTime=request.form['OverTime']
        if OverTime=='0':
            OverTime_Yes='0'
        elif OverTime=='1':
            OverTime_Yes='1'            
        else:
            pass

        StockOptionLevel=request.form['StockOptionLevel']
        if StockOptionLevel=='0':
            StockOptionLevel_1='0'
            StockOptionLevel_2='0'
            StockOptionLevel_3='0'
        elif StockOptionLevel=='1':
            StockOptionLevel_1='1'
            StockOptionLevel_2='0'
            StockOptionLevel_3='0'
        elif StockOptionLevel=='2':
            StockOptionLevel_1='0'
            StockOptionLevel_2='1'
            StockOptionLevel_3='0'
        elif StockOptionLevel=='3':
            StockOptionLevel_1='0'
            StockOptionLevel_2='0'
            StockOptionLevel_3='1'
        else:
            pass

        WorkLifeBalance=request.form['WorkLifeBalance']
        if WorkLifeBalance=='0':
            WorkLifeBalance_2='0'
            WorkLifeBalance_3='0'
            WorkLifeBalance_4='0'
        elif WorkLifeBalance=='1':
            WorkLifeBalance_2='1'
            WorkLifeBalance_3='0'
            WorkLifeBalance_4='0'
        elif WorkLifeBalance=='2':
            WorkLifeBalance_2='0'
            WorkLifeBalance_3='1'
            WorkLifeBalance_4='0'
        elif WorkLifeBalance=='3':
            WorkLifeBalance_2='0'
            WorkLifeBalance_3='0'
            WorkLifeBalance_4='1'
        else:
            pass


        features=[age,DailyRate,DistanceFromHome,EmployeeNumber,HourlyRate,MonthlyIncome,MonthlyRate,NumCompaniesWorked,PercentSalaryHike,TotalWorkingYears,TrainingTimesLastYear,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager,BusinessTravel_Travel_Frequently,BusinessTravel_Travel_Rarely,JobInvolvement_2,JobInvolvement_3,JobInvolvement_4,JobRole_Human_Resources,JobRole_Laboratory_Technician,JobRole_Manager,JobRole_Manufacturing_Director,JobRole_Research_Director,JobRole_Research_Scientist,JobRole_Sales_Executive,JobRole_Sales_Representative,JobSatisfaction_2,JobSatisfaction_3,JobSatisfaction_4,MaritalStatus_Married,MaritalStatus_Single,OverTime_Yes,StockOptionLevel_1,StockOptionLevel_2,StockOptionLevel_3,WorkLifeBalance_2,WorkLifeBalance_3,WorkLifeBalance_4]


        lst=map(lambda x: float(x), features)
        values=np.array(list(lst))
        values=values.reshape(1,-1)
        pred=model.predict(values)

        return render_template("result.html", pred=pred)


if __name__=='__main__':
  app.run(host='0.0.0.0',port=8080)