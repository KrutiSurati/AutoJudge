# AutoJudge: Predicting Programming Problem Difficulty
## **Project Overview**-

AutoJudge is a machine learning–based system designed to predict the difficulty of programming problems using only textual information.
Given a problem’s description, input description, and output description, the system:
Predicts the difficulty class (Easy / Medium / Hard)
Predicts a numerical difficulty score
Provides results through a simple web-based user interface
This project demonstrates the complete ML pipeline, including preprocessing, feature extraction, classification, regression, evaluation, and deployment via a web UI.


## **Dataset Used**-
```text
The dataset consists of programming problems collected from online competitive programming platforms. Each data sample contains the following fields:
•	“title”                       Problem name
•	“description”                 Detailed textual description of the problem
•	“input_description”           Textual Description of the input
•	“output_description”          Textual Description of the output
•	“sample_io”                   Sample for how input/output will be entered
•	“problem_class”               Problem classification into easy/medium/hard
•	“problem_score”               Score allotted based on difficulty
•	“url”                         Link to the problem
Only textual fields were used as inputs to satisfy project constraints.
```

## **Approach and Models Used**-

**1.Data Preprocessing**
```
Dropped unnecessary columns like sample_io andd url
Combined all text fields into a single feature (combined_text)
Checked and handled missing values
Cleaned text implicitly via TF-IDF preprocessing.
```

**2.Feature Extraction**
```
Used TF-IDF Vectorization
Parameters:
max_features = 5000
stop_words = "english"

This converted raw text into numerical feature vectors suitable for machine learning models.
```
**Model 1: Classification**
```
Objective: Predict difficulty class (Easy / Medium / Hard)
Model Used: Logistic Regression
Input: TF-IDF features
Output: Difficulty class
```
**Model 2: Regression**
```
Objective: Predict numerical difficulty score
Model Used: Linear Regression
Input: TF-IDF features
Output: Difficulty score

```
## **Evaluation Metrics**
Classification Performance
```
Accuracy: 50.5%
```
**Metrics Used**:

Confusion Matrix-
```bash
 [[ 24  64  48]
 [  7 314 104]
 [ 16 168  78]]
```
Precision, Recall, F1-score-
```
Classification Report:
               precision    recall  f1-score   support

        easy       0.51      0.18      0.26       136
        hard       0.58      0.74      0.65       425
      medium       0.34      0.30      0.32       262

    accuracy                           0.51       823
   macro avg       0.47      0.40      0.41       823
weighted avg       0.49      0.51      0.48       823
```
This performance is reasonable given:
Text-only prediction
Multi-class classification
Real-world noisy data

**Regression Performance**
```
MAE: 1.73
RMSE: 2.07
```
These metrics indicate acceptable prediction error for difficulty scoring.


## **Web Interface**-
A Streamlit-based web UI is provided.
**Features**:
Four input text boxes:

Problem Title, 
Problem Description, 
Input Description, 
Output Description & 
A Predict button

**Displays**:

Predicted difficulty class &
Predicted difficulty score. 
No authentication or database is required.
The application runs entirely locally.


 ## **Steps to Run the Project Locally**-
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
## **Saved Trained Models**-
The following trained models are included in the repository:
tfidf_vectorizer.pkl
difficulty_classifier.pkl
difficulty_regressor.pkl
These are loaded directly by the web interface for inference.


## **Demo Video**-
Demo Video Link:
https://drive.google.com/file/d/1ZlPIJHIljJNgPHYpsgcbMOAj2VGuCTr1/view?usp=drivesdk
The video demonstrates:
Project overview, 
Model pipeline, 
Running the web UI locally & 
Sample predictions


## **Details**-
Name: Kruti Surati (23119046)

Institute: Production and Industrial Engineering, B-Tech IIT Roorkee

Project: AutoJudge – Problem Difficulty Prediction


## **Conclusion**-

This project successfully implements an end-to-end machine learning system for predicting programming problem difficulty using only textual inputs. The solution meets all project requirements, including model training, evaluation, saved models, and a functional web interface.










