import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title('AI National Examination Prediction')
maths = st.number_input("Maths Result")
english = st.number_input("English Result")
civics = st.number_input("Civics Result")
chemistry = st.number_input("Chemistry Result")
biology = st.number_input("Biology Result")
physics = st.number_input("Physics Result")
GPAx = st.number_input("GPA")

column = ['maths','english', 'civics', 'chemistry', 'biology', 'physics', 'GPA']

def predict():
    row = np.array([maths,english,civics, chemistry, biology, physics,GPAx])
    X = pd.DataFrame([row], columns=column)
    prediction = model.predict(X)
    rez = 'Your Potential matric Result is ' + str(prediction)
   


    if prediction > 0:
        st.success(rez)
    else:
        st.error('Please enter values correctly')    

st.button('Predict', on_click=predict)