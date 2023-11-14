# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set a title for your app
st.title("My Streamlit App")

# Add a text message
st.write("Welcome to my Streamlit app!")

# Add a slider widget
age = st.slider("Select your age:", 0, 100, 25)
st.write("Your selected age:", age)

# Create a simple plot based on the age
x = np.arange(age)
y = x * 2  # A simple linear relationship for demonstration
plt.plot(x, y)
plt.xlabel("Age")
plt.ylabel("Double Age")
plt.title("Age vs. Double Age Plot")

# Display the plot in Streamlit
st.pyplot()
