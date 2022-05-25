
   
from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
app = Flask(__name__)

def recommend(code):
    print('call recommend')
    dataset=pd.read_csv("product_cnpm.csv", engine='python', error_bad_lines=False)
    dataset.head(130)
    print('dataset', dataset)
    return code

@app.route("/evaluate", methods=['POST'])
def hello_world():
    data = request.json
    code = data['name']
    result = {
        "name": "ok"
    }
    return recommend(result)

if __name__ == "__main__":
    app.run(port=8080,debug= True)         