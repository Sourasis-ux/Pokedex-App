# AI Pokédex: 143-Class Computer Vision System 

A real-time computer vision web application capable of accurately classifying 143 distinct classes with 83.69% validation accuracy and ~45ms inference time per image.

**Tech Stack:** TensorFlow, Keras, Python, Streamlit

**Core Architecture**
* **Model:** Deep Convolutional Neural Network (CNN) with 4.62M parameters.
* **Dataset:** Trained on a 17,200+ image dataset using advanced data augmentation techniques.
* **Optimization:** Implemented adaptive learning-rate scheduling for efficient convergence.

**Deployment & Performance**
* Deployed on Streamlit Cloud with persistent model caching (`@st.cache_resource`) to prevent out-of-memory (OOM) errors and reduce server overhead.
* Implemented efficient image sanitization protocols for seamless client-side interaction.
