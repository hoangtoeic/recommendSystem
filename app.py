
   
from flask import Flask, redirect, url_for, render_template, request
from Service.service import recommendRoot
app = Flask(__name__)


@app.route("/recommend", methods=['POST'])
async def hello_world():
    data = request.json
    productId = data['id']
    exceptProductID = data['exceptProductID']
    print ("exceptProductID", exceptProductID)
    ok = await recommendRoot(productId, exceptProductID)
    return ok

if __name__ == "__main__":
    app.run(port=8080,debug= True)         