# House Price Prediction (Bengaluru)

## Overview

This project predicts house prices in Bengaluru using machine learning. It covers the full pipeline from data cleaning and feature engineering to model training and a simple web interface built with Flask.

## Dataset

The dataset contains information such as location, size (BHK), total square feet, number of bathrooms, and price. It required significant preprocessing because of inconsistent formats and missing values.

## Data Preprocessing

* Removed irrelevant columns like availability and society
* Handled missing values in key fields
* Extracted BHK from the size column
* Cleaned total_sqft values (handled ranges and invalid formats)
* Created a new feature: price_per_sqft
* Removed outliers based on:

  * minimum area per BHK
  * abnormal price per square foot within each location
* Reduced rare locations by grouping them into "other"
* Applied one-hot encoding for categorical variables

## Model

Three models were tested:

* Linear Regression
* Decision Tree
* Random Forest

Random Forest gave the best performance and was selected for deployment.

## Evaluation

The model was evaluated using:

* R² score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

## Project Structure

house-price-app/

* app.py
* model/

  * model.pkl
  * columns.pkl
* templates/

  * index.html
* static/

  * style.css
  * script.js
* requirements.txt
* README.md

## Running the Project

1. Clone the repository:
   git clone https://github.com/your-username/house-price-prediction.git

2. Navigate to the project folder:
   cd house-price-prediction

3. Create a virtual environment:
   python -m venv venv

4. Activate the environment:
   Windows:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the application:
   python app.py

7. Open in browser:
   http://127.0.0.1:5000/

## Notes

* The model expects input features in the same format as used during training.
* columns.pkl is required to maintain feature consistency.
* The application currently uses a simple HTML interface.

## Future Improvements

* Add better UI design
* Deploy the app online
* Add more features such as area type and advanced filtering
* Improve model performance using hyperparameter tuning

## Author

Nikhil Sanga
