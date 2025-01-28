import streamlit as st 
import numpy as np
import pandas as pd 
import pickle

model=pickle.load(open('model.pkl','rb'))

## making the streamlit app
st.title("Student Package Predictor")
st.write("this app predicts your package using your cgpa and iq data")

cgpa=st.number_input("Enter your CGPA: ", min_value=0.0, max_value=10.0, step=0.1)
iq=st.number_input("enter your IQ: ",min_value=70,max_value=200,step=1)

st.button("predict Package")
if(iq>70 and cgpa>0):
    input_data = np.array([[cgpa, iq]])
    prediction=model.predict(input_data)

    if( prediction==1):
        st.success("congrats!! you are likely to be placed")
    else:
        st.error("work harder to get better results")

else:
    st.error("enter valid input")



