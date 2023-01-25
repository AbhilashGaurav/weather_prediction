import pickle
import streamlit as st
import numpy as np


loaded_model = pickle.load(open('trained_model_weather_predict.sav', 'rb')) # read binary  rb
# creating a function

def weather(input_data):
    input_data_asnumpy = np.asarray(input_data)

    # reshape input_data
    input_data_reshaped = input_data_asnumpy.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped) # here we have used our loaded model
    # print(prediction)
    if (prediction[0]=='rain'):
      return("🌧Rain")
    elif (prediction[0]=='drizzle'):
      return("Drizzle")
    elif (prediction[0]=='snow'):
      return("Snow🥶")
    elif (prediction[0]=='fog'):
      return("🌁Fog")
    elif (prediction[0]=='sun'):
      return("🌞Sun")

def main():
    # giving the title 
    st.title = "weather prediction webapp"
    # precipitation	temp_max	temp_min	wind
    precipitation = st.text_input("Precipitation of the day")
    temp_max = st.text_input("Maximum temperature of the day")
    temp_min = st.text_input("Minimum temperature of the day")
    wind = st.text_input("Wind value of the day")

    # code for the prediction
    calulation = ''

    # creating a button
    if st.button('weather prediction'):
        calulation = weather([precipitation ,temp_max,	temp_min, wind])
    st.success(calulation)

if __name__ == '__main__':
    main()

