import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Bankruptcy Prevention deployed By Shubham", page_icon=":guardsman:", layout="wide")

st.markdown(
    f"""
    <style>
         .stApp {{
             background-image: url("https://wallpapercave.com/wp/wp2019326.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.markdown(
    f"""
    <style>
    .title {{
        color: blue;
        font-weight: bold;
        text-align: center;
    }}
    .user-input-header {{
        color: blue;
        font-weight: bold;
    }}
    .user-input-value {{
        color: black;
        background-color: white;
    }}
    .predicted-result {{
        color: blue;
        font-weight: bold;
    }}
    .predicted-output {{
        background-color: blue;
        padding: 10px;
        border-radius: 10px; /* Change the value of border-radius to adjust the curvature of the corners */
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)




st.title('Bankruptcy Prevention')
st.markdown(
    """
    <style>
    h1 {
        text-align: center;
        font-weight: bold;
        color: RebeccaPurple;
    }
    </style>
    """, unsafe_allow_html=True
)

st.sidebar.header('User Input Parameters')

def user_input_features():
    industrial_risk = st.sidebar.selectbox('Industrial Risk',('1','0.5','0'))
    management_risk = st.sidebar.selectbox('Management Risk',('1','0.5','0'))
    financial_flexibility = st.sidebar.selectbox('Financial Flexibility',('1','0.5','0'))
    credibility = st.sidebar.selectbox('Credibility',('1','0.5','0'))
    competitiveness = st.sidebar.selectbox('Competitiveness',('1','0.5','0'))
    operating_risk = st.sidebar.selectbox('Operating Risk',('1','0.5','0'))
    data = {'industrial_risk':float(industrial_risk),
            'management_risk':float(management_risk),
            'financial_flexibility':float(financial_flexibility),
            'credibility':float(credibility),
            'competitiveness':float(competitiveness),
            'operating_risk':float(operating_risk)}
    features = pd.DataFrame(data,index = [0])
    return features 

df = pd.read_csv("C:\\Users\\SHUBHAM\\Desktop\\PROJECT 3\\bankruptcy_updated.csv")
df.columns = df.columns.str.strip()
df['class']=df['class'].map({'non-bankruptcy':0,'bankruptcy':1})


# Preprocessing
X = df.drop('class', axis=1)
y = df['class']

# Model training
model = RandomForestClassifier()
model.fit(X, y)

# Prediction
df = user_input_features()
st.subheader('User Input parameters')
st.markdown('<div class="user-input-header">User Input parameters</div>', unsafe_allow_html=True)
st.markdown('<div class="user-input-value">{}</div>'.format(df.to_html(index=False)), unsafe_allow_html=True)

# centered_button = st.empty()
# centered_button.write(
#     "<div style='display: flex; justify-content: center;'>"
#     "<button style='height:50px;width:150px;font-size:20px;background-color:Black;color:white;border-radius:10px;' id='check_result_button'>Check Result</button>"
#     "</div>", unsafe_allow_html=True)

# if centered_button.button('Check Result', key='check_result_button', help='Click to check if the company will go bankrupt.'):
#     y_pred = model.predict(df)
#     result = 'Company Going Bankrupt' if y_pred[0] == 1 else 'Company Not Going Bankrupt'
#     st.markdown('<div style="text-align:center;">'
#                 '<span style="font-weight:bold;color:Black;">{}</span></div>'.format(result), 
#                 unsafe_allow_html=True)


if st.button('Check Result', key='check_result_button', help='Click to check if the company will go bankrupt.'):
    y_pred = model.predict(df)
    result = 'Company Going Bankrupt' if y_pred[0] == 1 else 'Company Not Going Bankrupt'
    st.markdown("<div style='text-align: center; background-color: #f1f1f1;'>"
                "<h3 style='color: black;'>{}</h3>"
                "</div>".format(result), unsafe_allow_html=True)
