import streamlit as st
import pickle
import time

st.title("Twitter sentiment analysis")

#load model
model = pickle.load(open('twitter_sentiment_analysis.pkl','rb'))

tweet = st.text_input('enter your tweet')
submit = st.button('predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('prediction time taken:',round(end-start, 2),'seconds')
    print(prediction[0])
    st.write('predicted sentiment is: ', prediction[0])