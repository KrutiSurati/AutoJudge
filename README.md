AutoJudge: Predicting Programming Problem Difficulty
**Project Overview**-
AutoJudge is a machine learning–based system designed to predict the difficulty of programming problems using only textual information.
Given a problem’s description, input description, and output description, the system:
Predicts the difficulty class (Easy / Medium / Hard)
Predicts a numerical difficulty score
Provides results through a simple web-based user interface
This project demonstrates the complete ML pipeline, including preprocessing, feature extraction, classification, regression, evaluation, and deployment via a web UI.


**Dataset Used**-
The same dataset as given in the problem statement is used. Out of all the columnss -'title', 'description', 'input_description', 'output_description',
'sample_io', 'problem_class', 'problem_score', 'url' 
 these are the selected ones -
        "title",
        "description",
        "input_description",
        "output_description",
        "problem_class",
        "problem_score" 

Only textual fields were used as inputs to satisfy project constraints.


**Approach and Models Used**-

1.Data Preprocessing
Selected textual fields:
Problem description
Input description
Output description

Combined all text fields into a single feature (combined_text)
Checked and handled missing values
Cleaned text implicitly via TF-IDF preprocessing.

2.Feature Extraction-
Used TF-IDF Vectorization
Parameters:
max_features = 5000
stop_words = "english"

This converted raw text into numerical feature vectors suitable for machine learning models.

Model 1: Classification-

Objective: Predict difficulty class (Easy / Medium / Hard)
Model Used: Logistic Regression
Input: TF-IDF features
Output: Difficulty class

Model 2: Regression-

Objective: Predict numerical difficulty score
Model Used: Linear Regression
Input: TF-IDF features
Output: Difficulty score


Evaluation Metrics-
Classification Performance
Accuracy: 50.5%

**Metrics Used**:

Accuracy
Confusion Matrix
Precision, Recall, F1-score
This performance is reasonable given:
Text-only prediction
Multi-class classification
Real-world noisy data

Regression Performance-
MAE: 1.73
RMSE: 2.07
These metrics indicate acceptable prediction error for difficulty scoring.


**Web Interface**-
A Streamlit-based web UI is provided.
Features:
Four input text boxes:

Problem Title
Problem Description
Input Description
Output Description
A Predict button

Displays:
Predicted difficulty class
Predicted difficulty score
No authentication or database is required.
The application runs entirely locally.


**Steps to Run the Project Locally**-
1.Clone the Repository
```bash
git clone https://github.com/KrutiSurati/AutoJudge.git
cd AutoJudge
```
2.Install dependencies
```bash
pip install -r requirements.txt
```
3.Run the Web Application
```bash
streamlit run app.py
```
4.Open Browser
The app will automatically open at:
```bash
http://localhost:8501

```
**Saved Trained Models**-
The following trained models are included in the repository:
tfidf_vectorizer.pkl
difficulty_classifier.pkl
difficulty_regressor.pkl
These are loaded directly by the web interface for inference.


**Demo Video**-
Demo Video Link:
https://drive.google.com/file/d/1ZlPIJHIljJNgPHYpsgcbMOAj2VGuCTr1/view?usp=drivesdk
The video demonstrates:
Project overview
Model pipeline
Running the web UI locally
Sample predictions


**Details**-
**Name: Kruti Surati (23119046)
Institute: Production and Industrial Engineering, B-Tech IIT Roorkee
Project: AutoJudge – Problem Difficulty Prediction**


**Conclusion**-

This project successfully implements an end-to-end machine learning system for predicting programming problem difficulty using only textual inputs. The solution meets all project requirements, including model training, evaluation, saved models, and a functional web interface.

