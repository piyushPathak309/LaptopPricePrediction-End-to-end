import streamlit as st
import pickle
import numpy as np


pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

Company = st.selectbox("Brand", df['Company'].unique())

TypeName = st.selectbox("TypeName", df['TypeName'].unique())
Ram = st.selectbox("Ram in GB", [2, 4, 6, 8, 12, 16, 24, 32, 64])
Weight = st.number_input("Weight Of Laptop")

TouchScreen = st.selectbox('TouchScreen', ['No', 'Yes'])

Ips = st.selectbox('IPS', ['No', 'Yes'])
Screen_Size = st.number_input("Screen Size")

Resolution = st.selectbox('Screen Resolution', ['1920x1080',
                                                '1366x768',
                                                '1600x900',
                                                '3840x2160',
                                                '3200x1800',
                                                '2880x1800',
                                                '2560x1600',
                                                '2560x1440',
                                                '2304x1440'])
CPU = st.selectbox("CPU", df['CpuBrand'].unique())

HDD = st.selectbox("HDD(in GB)", [0, 128, 256, 512, 1024, 2048])

SSD = st.selectbox("SDD(in GB)", [0, 8, 128, 256, 512, 1024])

GPU = st.selectbox("GpuBrand", df['Gpu Brand'].unique())

OS = st.selectbox("OS", df['os'].unique())

if st.button("Predict Price"):
    ppi = None
    if TouchScreen == 'Yes':
        TouchScreen = 1
    else:
        TouchScreen = 0

    if Ips == "Yes":
        Ips = 1
    else:
        Ips = 0
    X_res = float(Resolution.split('x')[0])
    Y_res = float(Resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / float((Screen_Size))
    query = np.array([Company, Ram, TypeName, Weight, TouchScreen, Ips, ppi, CPU, HDD, SSD, GPU, OS])
    query = query.reshape(1, 12)
    st.title(np.exp(pipe.predict(query)))
