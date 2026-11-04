AI Pokédex: 143-Class Computer Vision System
A real-time computer vision web application capable of accurately classifying 143 distinct Pokémon classes with 83.69% validation accuracy and ~45ms inference time per image.
Tech Stack
Deep Learning: TensorFlow, Keras
Backend & UI: Python, Streamlit
Data Processing: NumPy, Pillow
Core Architecture
Model: Deep Convolutional Neural Network (CNN) scaling to 4.62M parameters.
Dataset: Trained on a 17,200+ image dataset using advanced data augmentation techniques to prevent overfitting and improve generalization.
Optimization: Implemented categorical cross-entropy loss and adaptive learning-rate scheduling for efficient convergence.
Deployment & Performance
Deployed on Streamlit Cloud with persistent model caching (@st.cache_resource) to prevent out-of-memory (OOM) errors and drastically reduce server compute overhead.
Implemented efficient image sanitization and resizing protocols for seamless client-side interaction.