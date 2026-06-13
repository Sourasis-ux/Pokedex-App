import streamlit as st
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# 1. Set up the Webpage
st.set_page_config(page_title="Custom Pokédex", page_icon="🔴")
st.title("🔴 AI Pokédex Vision System")
st.markdown("Upload a picture of a Gen-1 Pokémon, and my custom Convolutional Neural Network will identify it!")

# 2. Load the Brain & Class Names (Cached so it only loads once)
@st.cache_resource
def load_pokedex_model():
    return load_model('pokedex_model.keras')

model = load_pokedex_model()

# Load class names from the tiny text file instead of the massive dataset
with open('classes.txt', 'r') as f:
    class_names = [line.strip() for line in f.readlines()]

# 3. Create the Image Uploader
uploaded_file = st.file_uploader("Choose a Pokémon image...", type=["jpg", "png", "jpeg"])

# 4. The Inference Logic (Only runs if they upload an image)
if uploaded_file is not None:
    # Display the uploaded image on the screen
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_container_width=True)
    
    st.write("Scanning database...")
    
    # Format the image perfectly for our CNN
    img = img.resize((128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Predict!
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)
    predicted_pokemon = class_names[predicted_index]
    confidence = np.max(predictions) * 100
    
    # Display the final result in a massive green box
    st.success(f"**Prediction:** {predicted_pokemon}")
    st.info(f"**Confidence:** {confidence:.2f}%")