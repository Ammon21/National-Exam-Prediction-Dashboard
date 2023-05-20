import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title('AI National Examination Prediction')
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
    rez = 'Your Potential matric Result is ' + str(prediction)
   


    if prediction > 0:
        st.success(rez)
    else:
        st.error('Please enter values correctly')    

st.button('Predict', on_click=predict)
