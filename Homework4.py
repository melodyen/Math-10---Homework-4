#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:59:01 2021

@author: melodyen
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#Question 1
st.title("Math 10: HW 4")

#Question 2
st.markdown("[Melodye Nguyen] (https://github.com/melodyen)")

#Question 3
csv = st.file_uploader(label="Choose a CSV file, please!",type=["csv"])

#Question 4
#We want to convert the file to a pandas df
#But there will be an error if we don't have an uploaded file first
if csv is not None:
    df = pd.read_csv(csv)
    #If x is an empty string, make it numpy's not-a-number
    #otherwise, leave x alone
  
#Question 5
    df = df.applymap(lambda x: np.nan if x == " " else x)
    
#Question 6
    #See Week 3 Friday Lecture
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
        
    #Now, let's make a list of all the columns that can be made numeric
    
    good_cols = [c for c in df.columns if can_be_numeric(c)]

#Question 7
#Replace columns in df that can be made numeric with their numeric values
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)
    
#Question 8
    x_axis = st.selectbox("Select a value for the x-axis", good_cols)
    y_axis = st.selectbox("Select a value for the y-axis", good_cols)
    
#Question 9
    slider = st.slider("Row selected", 0 ,len(df.index)-1,(0,len(df.index)-1))
    
#Question 10
    st.write(f"{x_axis} and {y_axis} of {slider} is")
    
#Question 11
    spotify = alt.Chart(df.loc[slider[0]:slider[1]]).mark_circle().encode(
    x = x_axis, 
    y = y_axis,
    color = "Energy"
    )
    st.altair_chart(spotify)
    
#Question 12
#Added color to the altair chart and made it equal to the Energy values