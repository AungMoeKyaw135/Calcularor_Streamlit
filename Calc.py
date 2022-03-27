import numpy as np
import streamlit as st

st.title('Calculatar')

st.header('Signs')
st.write('Sum       => +')
st.write('Different => -')
st.write('Multiply  => * ')
st.write('Divide    => / ')
st.subheader('Calculating:')

ans = "None"

a = st.text_input('Enter First number: ','0')
a = int(a)

b = st.text_input('Enter Second number: ','0')
b = int(b)

c = st.text_input('Enter Sign')

if c == "+":
    ans = a + b

if c == "-":
    ans = a - b

if c == "*":
    ans = a * b

if c == "/":
    ans = a / b

if c == None:
    ans = "None"

st.write('Answer is :',ans)