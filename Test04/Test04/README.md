# Used Car Price Prediction using Supervised Machine Learning

---

## Problem Statement
---

The goal of this project is to build supervised machine learning models to predict the **selling price of used cars** using different features such as car name, manufacturing year, fuel type, transmission type, and kilometers driven.

This project also focuses on performing proper **data preprocessing and cleaning** before applying machine learning algorithms to improve prediction accuracy.

---

## Dataset Description
---

The dataset used in this project contains information about **used cars and their selling prices**. Each record represents a car with different attributes.

Important features in the dataset include:

- **name** – Car brand or model  
- **year** – Manufacturing year of the car  
- **selling_price** – Price at which the car is sold (**Target Variable**)  
- **km_driven** – Total kilometers driven by the car  
- **fuel** – Type of fuel used (Petrol, Diesel, CNG, etc.)  
- **seller_type** – Type of seller (Dealer or Individual)  
- **transmission** – Transmission type (Manual or Automatic)  
- **owner** – Ownership status of the car  
- **seats** – Number of seats in the car  
- **engine** – Engine capacity of the car  
- **max_power** – Maximum power produced by the engine  

---

## Data Cleaning and Preprocessing
---

The following preprocessing steps were applied before training the machine learning models:

- **Removed duplicate records** from the dataset  
- **Handled missing values** using median for numerical columns and mode for categorical columns  
- **Detected and removed outliers** using the IQR (Interquartile Range) method  
- **Encoded categorical variables** using Label Encoding  
- **Applied feature scaling** using StandardScaler  
- **Removed irrelevant columns** such as unnecessary index columns  
- **Split the dataset** into training and testing sets (80% training, 20% testing)

---

## Algorithms Used
---

The following supervised machine learning algorithms were used:

- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**

---

## Evaluation Metrics
---

The models were evaluated using the following regression metrics:

- **R² Score**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**

---

## Conclusion
---

This project demonstrates how supervised machine learning algorithms can be used to predict the selling price of used cars. Proper data preprocessing and cleaning significantly improve the performance of machine learning models. Among the implemented models, **Random Forest generally provides better prediction accuracy** compared to Linear Regression and Decision Tree.
