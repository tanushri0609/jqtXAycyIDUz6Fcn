### Happy Customer
## Introdustion:
One of the fastest growing start-ups in the logistics and delivery domain wants to predict if the user is happy or unhappy, based on the answers they provide for the survey questions.For this the company has given us a subset of a previous survey data. It consists of 7 columns and 126 rows. Based on this we need to build our prediction model.

## Data Description:
The CSV file contains 7 columns: X1 to X6 and Y. The description of each column is as follows:
* Y = Target attribute 
* X1 = My order was delivered on time
* X2 = Contents of my order was as I expected
* X3 = I ordered everything I wanted to order
* X4 = I paid a good price for my order
* X5 = I am satisfied with my courier
* X6 = The app makes ordering easy for me
Of these, X1 to X6 are feature attributes. These are 6 different questions the customer has to answer in the rank from 0 to 5.  Here 0 means least satisfied and 5 means highly satisfied. Hence, all feature attributes are numeric data.Y is the label. It contains binary value 0 and 1. Here, 0 refers to unhappy customer and 1 to happy customer. 

## Summary:
Project starts with EDA where we checked for null value and data imbalance. Also plot the relation between each feature with the label. Once we understand the data, we moved to feature selection. Here we perform correlation and EFS (Exhaustive Feature Selection) to select the best possible set of features for building our model. After that we built SVM, Logistic regression, Random Forest, and Xgboost Classifier.

## Conclusion:
As compare to other models Random Forest has given 0.8095 accuracy and the F1 score is 0.8260.
