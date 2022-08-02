# Churn-prediction-Deployment

### Predict the churn customer 

# Project Summary

### Mission: 1.Build machine learning model for clustering to find the groups clients and define their characteristics based on                            credit card customers dataset.
###                 2.Build an application that allows your customer to find the right group (cluster) for a given client. 

# Objectives: 
### Build machine learning model for clustering.
### Select the right performance metrics for your model.
### Tuning parameters of the model for better performance.
### Describe the results from unsupervised learning.
### Be able to deploy a machine learning model.
### Be able to create a Flask API that can handle a machine learning model.
### Create a basic Graphical User Interface to call the API
### eploy the API and the interface on Heroku


# Dataset:
### The dataset can be downloaded on the following link:

### https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

# Usage
## Files in this repo
### in preprocessing folder:
####        data_clean.ipynb: python file for data exploring, wrangling and cleaning, and get the final dataset for training
###         kmean_model.ipynb: contain the model 
### model_joblib.joblib file contain the model saved
### app.py the instance of Flask
### requirement.txt contains libraries 
### Dockerfile


# Workflow for this project
## Libraries used:
### pandas
### sklearn
### seaborn 
### matplotlib
### numpy
### flask

# Step 1 : Exploratory Data Analysis and Data Visualization

### Customer age distribution to see if customer age is normally distributed.
### Proportion of customer gender count (countplot and piechart)
### Proportion of existing and attrited customers count
### Proportion of existing and attrited customers by gender (countplot and piechart)
### Proportion of entire education levels
### Proportion of education level by existing and attrited customer
### Proportion of education level by gender (pieplot and countplot)
### Proportion of marital status by attrited and existing customers
### Proportion of income category
### Proportion of income category by customer
### Customer age count by customer
# Step 2 : Data cleaning
###               Drop 2 unnessary columns Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1
### Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2
###                Drop all the categorical data 


# Step3: Create Model and Cluster Data

### Use KMeans to cluster the customers based on their account activity, and then examine the numerical data of each group to see if they differ in a meaningful way.
### Use the elbow method to identify to find an optimal value for K to specify the number of clusters the algorithm will use.
### Use Principal Component Analysis to compress data 
###  Create a pipeline that will first process our data and then create a KMeans model.
### Calculate Silhoutte score 

# Step4:Deployment

### Deploy the model on flask 
### Deploy the model on Heroku







