from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and columns
model = pickle.load(open('model/house_price_model.pkl', 'rb'))
columns = pickle.load(open('model/columns.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs
        sqft = float(request.form['sqft'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        location = request.form['location']

        # Create dataframe with all columns
        input_df = pd.DataFrame(columns=columns)
        input_df.loc[0] = 0

        # Fill required values
        input_df['total_sqft'] = sqft
        input_df['bath'] = bath
        input_df['bhk'] = bhk

        # Set location column
        loc_col = "location_" + location
        if loc_col in input_df.columns:
            input_df[loc_col] = 1

        # Prediction
        prediction = model.predict(input_df)[0]

        return render_template(
            'index.html',
            prediction_text=f"Estimated Price: ₹ {round(prediction, 2)} Lakhs"
        )

    except Exception as e:
        print("Error:", e)
        return render_template(
            'index.html',
            prediction_text="Error in input"
        )

if __name__ == "__main__":
    app.run(debug=True)