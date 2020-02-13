# --------------
# Importing Necessary libraries
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score , f1_score
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the 20newsgroups dataset


#Create a list of 4 newsgroup and fetch it using function fetch_20newsgroups


#Use TfidfVectorizer on train data and find out the Number of Non-Zero components per sample.


#Use TfidfVectorizer on test data and apply Naive Bayes model and calculate f1_score.


#Print the top 20 news category and top 20 words for every news category




