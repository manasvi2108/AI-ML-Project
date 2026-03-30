# AI-ML-Project
The Mess Demand Predication System is a machine learning- based project that predicts 
the number of students likely to attend a college mess on a given day.
It uses factors like day of the week, exam schedule and special menu to estimate demand.
This helps in reducing food wastage and imporving resource planning.

FEATURES: 
1. Predicts daily mess demand
2. Stores historical attendance data in database
3. Learns continuously from new data
4. Uses Machine Learning (Linear Regression)

PREREQUISITES: 
Make sure you have "pip install pandas scikit-learn"

USAGE:
1. Run the program "python mess_predictor.py"
2. Enter:
   Day (1-7)
   Meny Type:
     1- Veg
     2-Mixed
     3-Special
3. Get Prediction
4. Enter actual attendance it will help improve the model over time 

PROJECT STRUCTURE:
 mess_predictor
  1. mess_predictor.py
  2. mess.db
  3. README.md
  
FUTURE IMPROVEMENTS:
1. Web Interface (Flask/Django)
2. Better ML models (Random Forest)
3. Real time IoT integration (actual CPS)
4. Menu based NLP analysis
