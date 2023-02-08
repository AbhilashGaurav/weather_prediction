import pickle
import streamlit as st
import numpy as np
# import style.css
with open ('style.css') as f:
			st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


loaded_model = pickle.load(open('trained_model_weather_predict.sav', 'rb')) # read binary  rb
# creating a function
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://qph.fs.quoracdn.net/main-qimg-9dc5f9eeb7965c3176a21690d284ab3e");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()
def weather(input_data):
    input_data_asnumpy = np.asarray(input_data)

    # reshape input_data
    input_data_reshaped = input_data_asnumpy.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped) # here we have used our loaded model
    # print(prediction)
    # st.image('demo_img.jpg')
    if (prediction[0]=='rain'):
      st.metric("Prediction","🌧","RAIN")
      # return("🌧Rain")
    elif (prediction[0]=='drizzle'):
      st.metric("Prediction","🌦️","Drizzle")
      # return("Drizzle")
    elif (prediction[0]=='snow'):
      st.snow()
      st.metric("Prediction","🥶","SNOW")
      # return("Snow🥶")
    elif (prediction[0]=='fog'):
      st.metric("Prediction","🌫️","FOG")
      # return("🌁Fog")
    elif (prediction[0]=='sun'):
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

