# Import libraries
import numpy as np
import pandas as pd
import streamlit as st

# Constant value
# THRESHOLD_RATING = 5.0 

data_food = pd.read_csv("data_food.csv")
list_name_food = [''] + list(data_food.name_food)
data_base = pd.read_csv("database.csv")

# Streamlit app
st.title("NAME APP")

st.header("WHAT SHOULD I COOKING TODAY?")
st.sidebar.header("LOGO")
input_name_food = st.sidebar.selectbox(label = 'I want to make: ',
                                  options = list_name_food, 
                                  format_func = lambda x: 'Type name food...' if x == '' else x)
st.markdown(
        """
    <style>
        div[role=radiogroup] label:first-of-type {
            visibility: hidden;
            height: 0px;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
input_method = st.sidebar.radio('Choose a method: ',
                                ['','Sentiment','SVD','LightFM'],
                                index=0)



if (input_name_food!='') & (input_method!=''):
    if (input_method=='Sentiment'):
        scores = pd.read_csv('Recommendations_Sentiment.csv')
    elif (input_method=='SVD'):
        scores = pd.read_csv('Recommendations_SVD.csv')
    else:
        scores = pd.read_csv('')
    
    input_id_food = data_food[data_food['name_food']==input_name_food].itemID.iloc[0]
    list_user_rated = np.array(data_base[(data_base.itemID == input_id_food)].sort_values('rating',ascending=False).userID)
    random_userID = np.random.choice(list_user_rated[:10])
    recommendations = scores[scores.userID==random_userID].sort_values('score', ascending=False)[['recommended_itemID','score']][:10]

    data_base["rn"] = data_base[['itemID','name_food','link_image_food','link_food']].groupby('itemID')['itemID'].rank(method='first')
    recommendations["rn"] = recommendations.groupby('recommended_itemID')['recommended_itemID'].rank(method='first')

    new_df = recommendations.merge(data_base[['itemID','name_food','link_image_food','link_food','rn']],
                                   left_on=['recommended_itemID','rn'],
                                   right_on=['itemID','rn'], 
                                   how='left')
    
    new_df.drop(['rn','itemID'],axis=1,inplace=True)

    st.write(new_df)

else:
    st.warning('Hmm..... No option is selected')
