# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import pandas as pd
from google.cloud import bigquery
import csv
import numpy as np
import pandas as pd

import os

credentials_path = 'data-key.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


client = bigquery.Client()

QUERY = ('SELECT YearsExperience,Salary FROM `melodic-bolt-327318.mldata1.test` LIMIT 1000')
query_job = client.query(QUERY) # API request
#query_job.to_csv("id.CSV",index= False)
rows = query_job.result()  # Waits for query to finish


header = ['YearsExperience', 'Salary']

array =[]
for row in rows:
    a =[]
    a.append(row.YearsExperience)
    a.append(row.Salary)
    array.append(a)
    
print(array)

with open('test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(array)
    
    
dataset = pd.read_csv('test.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

print(dataset)

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#print(dataset)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

dataset = pd.read_csv('test.csv')
X_test = dataset.iloc[:, :-1].values
y_test = dataset.iloc[:, 1].values


print(X_test)



# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
for value in y_pred:
    print(value)


#Upload data to bigquery

table_id = 'melodic-bolt-327318.mldata1.result'

for value in y_pred:
    rows_to_insert = [
     {u'salary':value},
     ]
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print('New rows have been added.')
    else:
        print(f'Encountered errors while inserting rows: {errors}')
    



    





