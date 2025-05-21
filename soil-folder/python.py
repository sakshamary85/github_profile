from flask import Flask, render_template, request
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)


model= pickle.load(open('random_forest_pkl.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    nitrogen=float(request.form['N'])
    phosphorus=float(request.form['P'])
    potassium=float(request.form['K'])
    ph=float(request.form['ph'])
    ec=float(request.form['ec'])
    oc=float(request.form['oc'])
    sulphur=float(request.form['S'])
    zinc=float(request.form['zn'])
    iron=float(request.form['fe'])
    copper=float(request.form['cu'])
    manganese=float(request.form['Mn'])
    barium=float(request.form['B'])
    result=model.predict([[nitrogen, phosphorus, potassium, ph, ec, oc, sulphur, zinc, iron, copper, manganese, barium]])# Replace with your actual prediction result
    return render_template('index.html',**locals())
        # return render_template('result.html', result=result)

        # return render_template('result.html', result=result)


  

if __name__ == '__main__':
    app.run(debug=True)
