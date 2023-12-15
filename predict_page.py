import streamlit as st
import pandas as pd
import pickle

def load_data():
    with open('HR_model.pkl', 'rb') as file:
        data = pickle.load(file)

    return data

data = load_data()

model = data["model"]
le_salary = data["le_salary"]


def show_predict_page():
    st.title(":rainbow[EXIT INSIGHT: A MACHINE LEARNING PREDICTOR FOR EMPLOYEE RETENTION]")
    satisfaction = st.slider(":blue[SATISFACTION LEVEL]", 0.09, 1.00, 0.25)
    hours = st.slider(":blue[AVERAGE MONTHLY HOURS]", 96, 310, 100)
    promotion = st.selectbox(":blue[PROMOTION WITHIN LAST 5 YEARS]", (0,1))
    salary = st.selectbox(":blue[SALARY CATEGORY]", ('low', 'medium', 'high'))
    btnAction = st.button(":rainbow[PREDICT]")

    if btnAction:
        predictors = pd.DataFrame({
        "satisfaction_level": [satisfaction],
        "average_montly_hours" : [hours],
        "promotion_last_5years": [promotion],
        "salary": [salary]
        })

        # st.dataframe(predictors)

        predictors.salary = le_salary.transform(predictors.salary)
         
        # st.dataframe(predictors)
        # st.write(predictors)

        result = model.predict(predictors)


        st.write(f"The employee might {':green[stay.]' if result==0 else ':red[leave.]'}")

        # def result_change():
        #     if result == 0:
        #         return 'stay.'
        #     else:
        #         return 'leave'
        
        # st.write(f"The employee might {result_change()}")




