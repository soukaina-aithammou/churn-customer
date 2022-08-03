# Churn-prediction-Deployment

### Predict the churn customer 

# Objectives:

### Mission: 1.Build machine learning model for clustering to find the groups clients and define their characteristics based on                            credit card customers dataset.
###                 2.Build an application that allows your customer to find the right group (cluster) for a given client. 


# Dataset:
### The dataset can be downloaded on the following link:

### https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

# Usage
## Files in this repo
### in preprocessing folder:
####        data_clean.ipynb: python file for data exploring, wrangling and cleaning, and get the             final dataset for training
###         kmean_model.ipynb: contain the model 
### ML model persist  in a joblib file model_joblib.joblib 
### flask files — index.html and app.py the instance of Flask
### index.html for providing inputs (or features) to the model
### requirement.txt add all of the dependencies for the flask app.
### Procfile to specify the commands that are executed by Heroku app on startup
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
#### log in on Heroku and create a new app
#### heroku container:push web --app <name_of_app>
#### heroku container:release web --app <name_of_app>











