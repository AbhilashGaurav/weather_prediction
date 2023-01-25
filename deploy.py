import pickle
import numpy as np
# import streamlit as st


# loading the save model
loaded_model = pickle.load(open('trained_model_weather_predict.sav', 'rb')) # read binary  rb
input_data = (2.5,4.4,2.2,2.2) #for rain
# input_data = (0.0,6.7,-2.2,1.4)  # for snow

#changing the input_data to numpy array
input_data_asnumpy = np.asarray(input_data)

# reshape input_data
input_data_reshaped = input_data_asnumpy.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped) # here we have used ou loaded model
# print(prediction)
if (prediction[0]=='rain'):
  print("Rain")
elif (prediction[0]=='drizzle'):
  print("Drizzle")
elif (prediction[0]=='snow'):
  print("Snow🥶")
elif (prediction[0]=='fog'):
  print("Fog")
elif (prediction[0]=='sun'):
  print("Sun")