# -*- coding: utf-8 -*-
# Import is highly dependent on your path variables
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

# Independent variables are the first three columns
# dependent variable vector is the last column
# we take all the entries of the dataset except the last
# column, and we do that with the syntax as shown below
# colon represents that we take all the entries of the dataset
# the syntax after the comma represents that we select all the 
# columns of the dataset, except (for which we use -ve sign) the last first column
X = dataset.iloc[:, :-1].values 

# Now we will create the dependent variable vector
y = dataset.iloc[:, 3].values

# mind the np.nan instead of NaN
# now the data is slightly rattled, there are some missing data
# also, in real life cases, there might be some other check on the data

"""
To handle missing data, there are some things we can do:
    1. We delete the entries.
    2. We replace the entries with the mean of the entries of the column.
    3. We replace it with the median of the column entries.
    4. We can use any utility function dedicated to the specific entry.
    
    You will see how the choice of these functions can affect the performance of your model :)
"""


# Lets do the mean thing with the data, we use the function mean already defined in the library sklearn
from sklearn.impute import SimpleImputer

# This is a class, lets create an object for the class
imputer = SimpleImputer(missing_values=np.nan,
                  strategy="mean")

# Lets fit this object to our matrix object
imputer = imputer.fit(X[:, 1:3]) # Notice the '3' instead of '2', this is because upper bound is excluded

# assigning it to imputer object itself fits it as imputer object
# Now we replace with the mean
# transform replaces missing data with mean of the column
# we put the columns we want and put that in the transform function
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Now it's done, you might want to use some other strategy, you're free to do that
# Try doing the same with some other strategy
# You can use your MTH102 knowledge to maximize the reliablility of the models

# Now we would need to encode the text in numbers too, for feeding it in equations

# This library we will be using is sklearn again. But we will be using LabelEncoder now
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()

# we will use this object on our country variables
labelencoder_X.fit_transform(X[:, 0]) # this returns the first column of the matrix encoded

# now assign it to the first column
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

# but there is some problem, someone ??

# There is no relational order between the countries
# So we need to prevent the models to learn that there is no such preference

# A method to tackle this is to use the dummy variables
# this will be handling the data in such a way that you create a set for the different elements and put '0', '1' for each of them, for each entry.

# for this, we will be needing another class, that's called OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float)

# now the variables are encoded with 3 columns as you can see from the variable explorer
# let's do the same with y too

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y) # we don't need to hotencode this one as it's an dependent variable.

# Now let's move on and split the data into Training set and Test set
# for a nice model, performance of the model should be almost similar for the both of them
# let's start then !

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) # we will build these
# Now we will train the datasets from the X_train to predict y_train and then we will test it on X_test, y_test
 





























