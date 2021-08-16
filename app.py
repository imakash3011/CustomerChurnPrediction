from flask import Flask, render_template, request, redirect
import pandas as pd
import customer


app = Flask(__name__)


# @app.route("/", methods = ['GET'])
# def hello_world():
#     return render_template('index.html')


# @app.route("/predict", methods = ['POST'])
# def predict():
#     res = request.form
    
#     data = pd.DataFrame.from_dict(res, orient='index').T
#     print(data)
#     # return data
#     return res, 200 

@app.route("/predict", methods = ['POST'])
def predict():
    if request.method == 'POST':
        res = request.form
        #data = pd.DataFrame.from_dict(res, orient='index').T
        #print(data)
        x = customer.get_data(res)
        if x[0] == 0:
            result = "customer will not leave"
        else:
            result = "customer will leave"
        return render_template('result.html', result = result)

@app.route("/", methods = ['GET', 'POST'])
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)