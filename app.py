import numpy as np
import pandas as pd
import nltk
import string
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
import streamlit as st
import pickle

def transform_texts(text):
 text=text.lower()
 text=nltk.word_tokenize(text)
 y=[]
 for i in text:
     if i.isalnum():
      y.append(i)
 text=y[:] #if done by direct assignment it will copy reference
 y.clear()
 for i in text:
     if i not in stopwords.words('english') and i not in string.punctuation:
         y.append(i)
 text=y[:]
 y.clear()
 for i in text:
     y.append(ps.stem(i)+" ")
    

 return "".join(y)
# importing model from the library
tfdif=pickle.load(open('vectorizer.pkl','rb'))
# 
model=pickle.load(open('mnb.pkl','rb'))
print(model)

st.title('Email/SMS Spam Classifier')

inp_text=st.text_input('Enter the Email/SMS')
if st.button('Predict'):
# preprocessing data getting from the site
    transformed_text=transform_texts(inp_text)
#vectorize 
    vector_input=tfdif.transform([transformed_text])
# prediction

    result=model.predict(vector_input)[0]
    # display
    if(result==1):
        st.header('spam')
    else :st.header('not spam')



 