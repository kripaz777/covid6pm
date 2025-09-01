import streamlit as st
import pandas as pd
import pickle as pk
st.title("Salary Prediction System")
st.image("https://pianalytix.com/wp-content/uploads/2020/12/Salary-Prediction-Model-using-ML-1024x427.jpg")

#load model
load_model = pk.load(open('salary.pickle', 'rb'))

#input data from user
age = st.number_input("Enter your age = ",18,60)
exp = st.number_input("Enter Years of experience = ",0,40)
gender = st.radio("Gender = ", ["Male", "Female"])
edu = st.selectbox("Education = ", ["Bachelor",	"Master","PhD"])

if gender == 'Male':
    male = True
else:
    male = False

if edu == "Bachelor":
    b = 1; m = 0; p = 0
elif edu == "Master":
    b =0; m = 1; p = 0
else:
    b = 0; m= 0; p =1

# Age	Years of Experience	Male	Bachelor's	Master's	PhD
if st.button("Predict"):
    df = pd.DataFrame({
        'Age': [age],
        'Years of Experience':[exp],
        'Male':[male],
        "Bachelor's":[b],
        "Master's":[m],
        "PhD":[p]
    })
    st.dataframe(df)
    result = load_model.predict(df)
    st.balloons()
    
    st.write("Your salary is = ",int(result.tolist()[0][0]))