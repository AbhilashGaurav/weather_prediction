import pickle
import streamlit as st
import numpy as np
import sklearn as sklearn
# import style.css
with open ('style.css') as f:
			st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


loaded_model = pickle.load(open('trained_model_weather_predict.sav', 'rb')) # read binary  rb
# creating a function
image1 = "https://qph.fs.quoracdn.net/main-qimg-0c818b49cc2aeff5207add0d992d107f"
def add_bg_from_url(image1):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url(""" + image1 + """); # bg
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url(image1)
def weather(input_data):
    input_data_asnumpy = np.asarray(input_data)

    # reshape input_data
    input_data_reshaped = input_data_asnumpy.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped) # here we have used our loaded model
    # print(prediction)
    # st.image('demo_img.jpg')
    if (prediction[0]=='rain'):
      add_bg_from_url("https://qph.fs.quoracdn.net/main-qimg-b30c852193758aa7c610d46ebb12e8e9") #rain 
      st.metric("Prediction","🌧","RAIN")
      # return("🌧Rain")
    elif (prediction[0]=='drizzle'):
      add_bg_from_url("https://qph.fs.quoracdn.net/main-qimg-c6d657aa4a6e79e6c72e002af21588d2"); # dizzle
      st.metric("Prediction","🌦️","Drizzle")
      # return("Drizzle")
    elif (prediction[0]=='snow'):
      add_bg_from_url("https://qph.fs.quoracdn.net/main-qimg-ce8e51d79c26fd4f33566fcf09bef9dd"); # dizzle
      st.snow()
      st.metric("Prediction","🥶","SNOW")
      # return("Snow🥶")
    elif (prediction[0]=='fog'):
      add_bg_from_url("https://qph.fs.quoracdn.net/main-qimg-bf4d3fb5ec0e220423685a1b58900314"); # dizzle
      st.metric("Prediction","🌫️","FOG")
      # return("🌁Fog")
    elif (prediction[0]=='sun'):
      add_bg_from_url("https://qph.fs.quoracdn.net/main-qimg-2016f298e7d48626cf591be438c7d37c"); # dizzle
      st.metric("Prediction","🌞","SUN")
      # return("🌞Sun")
            

def main():
    # giving the title 

    st.title = "weather prediction webapp"
    # st.metric("temperature",42,2)
    # precipitation	temp_max	temp_min	wind
    with st.container():
      precipitation = st.text_input("Precipitation of the day",'5.3')
      temp_max = st.text_input("Maximum temperature of the day",'-1.1')
      temp_min = st.text_input("Minimum temperature of the day",'-3.3')
      wind = st.text_input("Wind value of the day",'3.2')

    # code for the prediction
    calulation = ''

    # creating a button
    if st.button('weather prediction'):
        calulation = weather([precipitation ,temp_max,	temp_min, wind])
    # st.success(calulation)


if __name__ == '__main__':
    main()

