# Getting-admitted-in-to-University- Linear Regression
Project Summary: Probability of Admission Prediction Using Linear Regression

This project aims to predict the probability of admission to a university based on various features such as GRE Score, TOEFL Score, University Rating, SOP, LOR, CGPA, and Research involvement. We used a **Linear Regression** model to make predictions.

### Key Steps Taken:
1. **Dataset Overview:**
   - The dataset consists of features like GRE Score, TOEFL Score, University Rating, SOP, LOR, CGPA, and Research involvement.
   - The target variable, initially named "Chance of Admit," was renamed to "Probability" to better represent the predicted values.

2. **Data Cleaning & Preprocessing:**
   - Dropped the **Serial No** column as it was not relevant for prediction.
   - Corrected the "Chance of Admit" column to reflect **probabilities**.
   - Performed **Exploratory Data Analysis (EDA)** to understand the data better.
   - Ensured that there were **no null values** in the dataset.
   - Removed **duplicates** and replaced any **0 values** with **NaN** where appropriate.

3. **Model Training:**
   - Applied **Linear Regression** for predicting the probability of admission.
   - Used **GridSearchCV** with a **for loop** to find the best random state for model training, optimizing performance with random state = 5.

4. **Deployment:**
   - Deployed the model using **Flask** to create a simple web application that predicts the probability of admission based on user input.

