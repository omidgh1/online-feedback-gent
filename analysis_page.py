import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from utils.Mongo import db_update, db_data
from utils.form_analysis import create_plots

st.set_option('client.showErrorDetails', False)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")
@st.cache(allow_output_mutation=True)
def get_mongo_client():
    user_name = "onlinefeedback_gent"
    password = "Qu10mxMGOsFx4lHb"
    uri = f"mongodb+srv://{user_name}:{password}@cluster0.sry1dls.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

client = get_mongo_client()

collection = client['Feedback']['Gent']
data = db_data(collection)
museum = data[data['section']=='Gravensteen'][['section','how_hear','motivation','score','idea','time']]
park = data[data['section']=='Citadelpark'][['section','how_often','activity','score','idea','time']]


st.header("Analysis Dashboard")
sector = st.radio('which place do you want to see its analysis?',options=['Citadelpark', 'Gravensteen'])
st.title(sector)
if sector == 'Gravensteen':
    create_plots(df=museum,var='how_hear',section=sector)
elif sector == 'Citadelpark':
    create_plots(df=park,var='how_often',section=sector)