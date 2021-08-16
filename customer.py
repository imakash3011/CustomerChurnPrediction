# import app
import pandas as pd
import numpy as np
# import json
import pickle
# from pandas.io import pickle


def get_data(res):
    dummies_df = predval()
    response = dict(res)

    for key in response:
        dummies_df[key] = response[key]
    
    lst = ['Contract', 'InternetService', 'PaymentMethod']
    dummies_df = dummies_df.drop(lst, axis=1)

    # print(dummies_df.T)
    # print(dummies_df.shape)

    for i in response:

        val = response[i]

        if val.endswith("Fiber optic"):
            dummies_df['InternetService_Fiber optic'] = 1
        if val.endswith("No"):
            dummies_df['InternetService_No'] = 1

        if val.endswith("One year"):
            dummies_df['Contract_One year'] = 1
        if val.endswith("Two year"):
            dummies_df['Contract_Two year'] = 1

        if val.endswith("Credit card (automatic)"):
            dummies_df['PaymentMethod_Credit card (automatic)'] = 1
        if val.endswith("Electronic check"):
            dummies_df['PaymentMethod_Electronic check'] = 1
        if val.endswith("Mailed check"):
            dummies_df['PaymentMethod_Mailed check'] = 1

    
    #dummies_df
    # print(main_df)
    # load the model from disk
    loaded_model = pickle.load(open('model.sav', 'rb'))
    return loaded_model.predict(dummies_df)



# filename = "model.sav"
# load_model = pickle.load(open(filename, 'rb'))
# model_score = load_model.predict(main_df)
# print(model_score)

    
def customer():
    Gender = ['Female', 'Male']
    Partner = ['Yes','No']
    Dependents = ['Yes','No']
    PhoneService = ['Yes','No']
    MultipleLines = ['Yes','No']
    OnlineBackup = ['Yes','No']
    DeviceProtection = ['Yes','No']
    InternetService = ['No', 'DSL','Fiber optic']
    OnlineSecurity = ['Yes','No']
    TechSupport  = ['Yes','No']
    StreamingTV  = ['Yes','No']
    StreamingMovies  = ['Yes','No']
    Contract =  ['Month-to-month', 'One year' ,'Two year']
    PaperlessBilling = ['Yes','No']
    PaymentMethod  =  ['Bank transfer (automatic)', 'Credit card (automatic)' , 'Mailed check', 'Electronic check']


    df = pd.DataFrame([Gender, Partner, Dependents, PhoneService, MultipleLines, OnlineBackup, DeviceProtection, InternetService, OnlineSecurity,TechSupport, StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod ]).T

    df.columns = ['Gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineBackup', 'DeviceProtection', 'InternetService', 'OnlineSecurity','TechSupport', 'StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod' ]
   
    df['Gender'].replace({"Male": 0, "Female":1}, inplace=True)
    
    df = df.fillna(0)

    two_cat = ['Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling']
    for i in two_cat:
        df[i].replace({"No":int('0'), np.nan:int('0'), "Yes": int('1')}, inplace=True)
        
    df['Gender'] = df.Gender.astype(int)
    
    # print(df)
    return df

def mydummies():
    df1 = customer()

    more_than2_val =  ['InternetService' ,'Contract' ,'PaymentMethod']
    df1 = pd.get_dummies(data=df1, columns = more_than2_val)
    # data.dtypes

    df1 = df1.drop(columns=['InternetService_DSL', 'InternetService_0'], axis=1)
    df1 = df1.drop(columns=['Contract_Month-to-month', 'Contract_0'], axis=1)
    df1 = df1.drop(columns=['PaymentMethod_Bank transfer (automatic)'], axis=1)

    dat=df1.head(1)

    for col in dat.columns:
        dat[col].values[:] = 0

    # print(dat)
    # print(dat.shape)

    return dat



def predval():
    dat = mydummies()
    # print(dat.info())
    # print(dat.shape)
    return dat


predval()
