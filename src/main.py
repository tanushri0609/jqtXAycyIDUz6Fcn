#Import the libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
from mlxtend.feature_selection import ExhaustiveFeatureSelector
import numpy as np


def read_csv():
    """
    Read the csv file and load the data frame into pandas

    Parameters
    ----------
    path : string
        This is the address of the csv file.

    Returns
    -------
    data_frame : 
        The pandas data frame.

    """
    data_frame=pd.read_csv('..\data\ACME-HappinessSurvey2020.csv', encoding = 'unicode_escape', sep=',', header=0)
    return(data_frame)

def understand_data(p_file):
    """
     This performs Exploratory Data Analysis on data frame.
    
    Parameters
    ----------
    p_file : Pandas data frame.
   """
   
    print('Shape of data:',data_frame.shape)
    
    # Check for Null Data
    print(data_frame.info())
    
    # Visulize the relation between two columns
    sb.pairplot(data_frame, palette='husl')
    plt.show()
    
    # check the effect of x1[my order was delivered on time] on y 
    data_frame.groupby(['X1','Y']).size().plot.bar(color=('r'))
    plt.show()
    
    # check the effect of x2 [contents of my order was as I expected] on y 
    data_frame.groupby(['X2','Y']).size().plot.bar(color=('r','b'))
    plt.show()
    
    # check the effect of x3 [I ordered everything I wanted to order] on y 
    data_frame.groupby(['X3','Y']).size().plot.bar(color=('r','b'))
    plt.show()
    
    # check the effect of x4 [I paid a good price for my order] on y 
    data_frame.groupby(['X4','Y']).size().plot.bar(color=('b','r'))
    plt.show()
    
    # check the effect of x5 [I am satisfied with my courier] on y 
    data_frame.groupby(['X5','Y']).size().plot.bar(color=('r','b'))
    plt.show()
    
    # check the effect of x6 [the app makes ordering easy for me] on y 
    data_frame.groupby(['X6','Y']).size().plot.bar(color=('r','b'))
    plt.show()
    return()

data_frame = read_csv()

understand_data(data_frame)

feature_selection()