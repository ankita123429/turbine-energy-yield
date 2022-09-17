# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 05:39:47 2022

@author: Rajat Panagria
"""

import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model=pickle.load(open('B:/Ankitacdac/project-deployment-streamlite/random_forest_regression_model.pk1','rb'))


#creating a function for  prediction

def totalYieldPrediction(input_data):
    #input_data = (4.5878,1018.7,83.675,3.5758,23.979,1086.2,11.898,0.32663,81.952)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():
    
    #giving the title
    st.title('total yeild prediction')
    
    #input data from user
    
    AT = st.text_input('Ambient temperture')
    AP = st.text_input('Ambient Pressure')
    AH = st.text_input('Ambient Humidity')
    AFDP = st.text_input('Air filter difference pressure')
    GTEP = st.text_input('Gas turbine  exhaust pressure')
    TIT = st.text_input('Turbine inlet pressure')
    CDP = st.text_input('Compresor discharge pressure')
    CO = st.text_input('carbon monoxide')
    NOX = st.text_input('Nitogen oxide')
    
    
    #code for prediction
    
    predicted_value=""
    
    #creating a button for prediction
    
    if st.button('TotalEnergy yield'):
        predicted_value =  totalYieldPrediction([AT, AP, AH, AFDP, GTEP,TIT,CDP, CO, NOX])
        
   
    st.success(predicted_value)


if __name__ =='__main__':
   main()    