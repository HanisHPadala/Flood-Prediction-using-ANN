from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
import numpy as np

model = load_model('model.h5')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET']) 
def predict():
    return render_template('prediction.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':
        MonsoonIntensity = float(request.form['MonsoonIntensity'])
        TopographyDrainage = float(request.form['TopographyDrainage'])
        RiverManagement = float(request.form['RiverManagement'])
        Deforestation = float(request.form['Deforestation'])
        Urbanization = float(request.form['Urbanization'])
        ClimateChange = float(request.form['ClimateChange'])
        DamsQuality = float(request.form['DamsQuality'])
        Siltation = float(request.form['Siltation'])
        AgriculturalPractices = float(request.form['AgriculturalPractices'])
        Encroachments = float(request.form['Encroachments'])
        IneffectiveDisasterPreparedness = float(request.form['IneffectiveDisasterPreparedness'])
        DrainageSystems = float(request.form['DrainageSystems'])
        CoastalVulnerability = float(request.form['CoastalVulnerability'])
        Landslides = float(request.form['Landslides'])
        Watersheds = float(request.form['Watersheds'])
        DeterioratingInfrastructure = float(request.form['DeterioratingInfrastructure'])
        PopulationScore = float(request.form['PopulationScore'])
        WetlandLoss = float(request.form['WetlandLoss'])
        InadequatePlanning = float(request.form['InadequatePlanning'])
        PoliticalFactors = float(request.form['PoliticalFactors'])

        features = [MonsoonIntensity, TopographyDrainage, RiverManagement, Deforestation, Urbanization, ClimateChange,
                    DamsQuality, Siltation, AgriculturalPractices, Encroachments, IneffectiveDisasterPreparedness,
                    DrainageSystems, CoastalVulnerability, Landslides, Watersheds, DeterioratingInfrastructure,
                    PopulationScore, WetlandLoss, InadequatePlanning, PoliticalFactors]
        print(features)

        inp = np.array([features])
        prediction = model.predict([inp])
        print(prediction[0][0])
        if prediction[0][0] >= 0.5:
            result = 'Flood'
        else:
            result = 'No Flood'
        return render_template('prediction.html', prediction_text=result, prediction_value=prediction[0][0])


@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

if __name__ == '__main__':
    app.run(debug=True)
