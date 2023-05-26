import streamlit as st
import numpy as np
import pandas as pd
import math


import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.image('cover.jpg')
st.title('AI National Examination Prediction System')
Maths = st.number_input("Maths Result")
English = st.number_input("English Result")
Civics = st.number_input("Civics Result")
Chemistry = st.number_input("Chemistry Result")
Biology = st.number_input("Biology Result")
Physics = st.number_input("Physics Result")
GPAx = st.number_input("GPA")

column = ['Maths','English', 'Civics', 'Chemistry', 'Biology', 'Physics', 'GPA']

def predict():
    row = np.array([Maths,English,Civics,Chemistry,Biology, Physics,GPAx])
    X = pd.DataFrame([row], columns=column)
    prediction = model.predict(X)
    return prediction


prediction = predict() 


def predictx(): 

    if prediction[0] > 0 and prediction[0] < 670:
        math.trunc(prediction[0])
    else:
        st.error('Please enter values correctly')  


st.markdown("<span style='color:red;font-size:18mm'>" + str(math.trunc(prediction[0])) + "</span>", 
               unsafe_allow_html=True)

