# from flask_wtf import FlaskForm
# from wtforms import SubmitField,SelectField,validators,FloatField
# from wtforms.fields.html5 import DateField,IntegerRangeField

# class SignUpForm(FlaskForm):
    
#     gender = ['Female', 'Male']
#     Partner = ['Yes','No']
#     Dependents = ['Yes','No']
#     PhoneService = ['Yes','No']
#     MultipleLines = ['Yes','No']
#     OnlineBackup = ['Yes','No']
#     DeviceProtection = ['Yes','No']
#     InternetService = ['No', 'DSL','Fiber optic']
#     OnlineSecurity = ['Yes','No']
#     TechSupport  = ['Yes','No']
#     StreamingTV  = ['Yes','No']
#     StreamingMovies  = ['Yes','No']
#     Contract =  ['Month-to-month', 'One year' ,'Two year']
#     PaperlessBilling = ['Yes','No']
#     PaymentMethod  =  ['Bank transfer (automatic)', 'Credit card (automatic)' , 'Mailed check', 'Electronic check']



#     gender = SelectField('Select gender ', choices=gender)
#     Partner = SelectField('Select Partner', choices=Partner)
#     Dependents = SelectField('Select Dependents', choices=Dependents)
#     PhoneService = SelectField('Select PhoneService', choices=PhoneService)
#     MultipleLines = SelectField('Select MultipleLines', choices=MultipleLines)
#     OnlineBackup = SelectField('Select OnlineBackup ', choices=OnlineBackup)
#     DeviceProtection = SelectField('Select DeviceProtection ', choices=DeviceProtection)
#     InternetService = SelectField('Select InternetService ', choices=InternetService)
#     OnlineSecurity = SelectField('Select OnlineSecurity ', choices=OnlineSecurity)
#     TechSupport  = SelectField('Select TechSupport ', choices=TechSupport)
#     StreamingTV  = SelectField('Select StreamingTV ', choices=StreamingTV)
#     StreamingMovies  = SelectField('Select StreamingMovies ', choices=StreamingMovies)
#     Contract =  SelectField('Select Contract ', choices=Contract)
#     PaperlessBilling = SelectField('Select PaperlessBilling ', choices=PaperlessBilling)
#     PaymentMethod  =  SelectField('Select PaymentMethod ', choices=PaymentMethod)

#     tenure = IntegerRangeField('Enter Total Duration', validators=[validators.Required()])
#     MonthlyCharges = FloatField('Enter Total Duration', validators=[validators.Required()])
#     TotalCharges = FloatField('Enter Total Duration', validators=[validators.Required()])
#     SeniorCitizen = IntegerRangeField('Enter Total Duration', validators=[validators.Required()])


#     submit = SubmitField(' Calculate Total Flight Fare! ')