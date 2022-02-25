from cgi import test
from copyreg import pickle
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline, Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import AdaBoostClassifier
import pickle



data=pd.read_csv("HR-Employee-Attrition.csv")


#label encoding the target variable
data['Attrition']=data['Attrition'].replace('No',0).astype("category")
data['Attrition']=data['Attrition'].replace('Yes',1).astype("category")

#changing data types
data['JobInvolvement']=data['JobInvolvement'].astype('object')
data['JobSatisfaction']=data['JobSatisfaction'].astype('object')
data['StockOptionLevel']=data['StockOptionLevel'].astype('object')
data['WorkLifeBalance']=data['WorkLifeBalance'].astype('object')


#extracting the  depemndent and indenpende variables
x=data[['Age', 'DailyRate', 'DistanceFromHome', 'EmployeeNumber', 'HourlyRate',
       'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
       'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
       'YearsWithCurrManager', 'BusinessTravel',
       'JobInvolvement', 'JobRole',
       'JobSatisfaction', 'MaritalStatus', 'OverTime',
       'StockOptionLevel', 'WorkLifeBalance']]

y=data['Attrition']

#one hot encoding the categorical features in independent variable
numerical=x.select_dtypes(np.number)
categorical=x.select_dtypes("object")
dummies=pd.get_dummies(categorical,drop_first=True)
dummy_variables=pd.concat([numerical,dummies], axis=1)


#reassigning the independent variables
x=dummy_variables.copy()

#splitting the training and test data
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.8,random_state=10)

#treating the imbalance nature of the data
smote = SMOTE(random_state = 10)
X_train_over, Y_train_over = smote.fit_resample(X_train, Y_train)

# def make_predictions(test):
#        scaler=StandardScaler()
#        scaler.fit_transform(X_train_over)
#        scaled_feature=scaler.transform(test)

#        model=AdaBoostClassifier(random_state=10)
#        model=model.fit(X_train_over)

#        return model.predict(scaled_feature)


# make_predictions(test)

#defing pipeline

pipe=Pipeline([('scaler', StandardScaler()), ('model', AdaBoostClassifier(random_state=10))])
pipe.fit(X_train_over,Y_train_over)
print(pipe.predict(X_test))

#saving model to disk
pickle.dump(pipe,open('model.pkl','wb'))

#read the model to comapare
model=pickle.load(open('model.pkl','rb'))

