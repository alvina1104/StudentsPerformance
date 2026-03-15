import streamlit as st
import requests

api_url = "http://127.0.0.1:8000/predict"


st.title('Predict Student Writing Score')
gender = st.selectbox('Gender:', ['male', 'female'])
race = st.selectbox('Race:', ['group A', 'group B', 'group C', 'group D', 'group E'])
parental = st.selectbox('Parental:', ["bachelor's degree", "high school", "master's degree",
                                      "some college", "some high school", "associate's degree"])
lunch = st.selectbox('Lunch:', ['standard', 'free/reduced'])
test = st.selectbox('Test:', ['completed', 'none'])
math_score = st.number_input('Math scores:', value=0)
reading_score = st.number_input('Reading scores:', value=0)


student_data = {
  "gender": gender,
  "race_ethnicity": race,
  "parental": parental,
  "test": test,
  "lunch": lunch,
  "math_score": math_score,
  "reading_score": reading_score
}

if st.button('Predict'):

    try:
        answer = requests.post(api_url, json=student_data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f'Result: {result.get('Writing_score')}')
            #st.json(result)

        else:
            st.error(f'Error : {answer.status_code}')
    except requests.exceptions.RequestException:
        st.error(f'Failed to connect to API')
