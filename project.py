import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title ("ALI's Penguins")
st.markdown ('Use this Streamlit app to make your own scatterplot about penguins!')
selected_penguins= st.selectbox ('What penguins would you like to visualize?',
['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_axis= st.selectbox ('What do want the x_axis to be?',
['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g'])
selected_y_axis = st.selectbox ('What about the y_axis?',
['bill_depth_mm', 'bill_length_mm',
'flipper_length_mm','body_mass_g']) 
penguins_df= pd. read_csv ('panguins.csv')
penguins_df= penguins_df[penguins_df ['species'] == selected_penguins]
figure,axe= plt.subplots ()
axe=sns.scatterplot (x = penguins_df [selected_x_axis], y =
penguins_df [selected_y_axis])
plt.xlabel (selected_x_axis)
plt.ylabel (selected_y_axis)
plt.title('Scatterplot of () species)) Penguins' .format
(selected_penguins))
st.pyplot(figure)