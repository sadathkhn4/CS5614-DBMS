import os
import random
import streamlit as st
import pandas as pd
from PIL import Image
import tensorflow as tf
import numpy as np

# Load CSV file with image details and color codes
csv_filename = 'output_info_colour.csv'  # Replace with your CSV file containing color information
df = pd.read_csv(csv_filename)

# Load the trained model for image classification
@st.cache(allow_output_mutation=True)
def load_my_model():
    model = tf.keras.models.load_model("mod.h5")  # Replace "mod.h5" with your trained model file
    return model

model = load_my_model()

# Streamlit app layout
st.title("Image Retrieval")

# Option for class selection or image upload for prediction
option = st.radio("Choose an option:", ("Select a class", "Upload an image"))

if option == "Select a class":
    # Class selection
    selected_class = st.selectbox("Select a class:", df['Class'].unique())

    # Filter data based on user-selected class
    filtered_data = df[df['Class'] == selected_class]

    # Get unique dominant colors for the selected class
    unique_colors_for_class = filtered_data['Dominant Color'].unique()

    # Color selection for the selected class
    selected_color = st.selectbox("Select a dominant color:", ['Any'] + list(unique_colors_for_class))

    # Filter filenames based on selected class and color
    if selected_color != 'Any':
        filtered_filenames = filtered_data[filtered_data['Dominant Color'] == selected_color]['File Name']
        has_selected_color = len(filtered_filenames) > 0
    else:
        filtered_filenames = filtered_data['File Name']
        has_selected_color = True

    # Display images based on selected class and color
    if st.button("Search"):
        st.header("Matching image:")
        found_image = False

        # Get all images in the specified class (without subfolders)
        all_images = os.listdir('100_images')  # Assuming all images are in the '100_images' folder
        all_images = [img for img in all_images if img.endswith(('.jpg', '.jpeg', '.png'))]

        # Filter available images based on selected class and color
        available_images = [img for img in all_images if img in filtered_filenames.values]

        # Display any available image from the selected class and color
        if has_selected_color and available_images:
            random_image = random.choice(available_images)
            image_path = os.path.join('100_images', random_image)
            if os.path.exists(image_path):
                img = Image.open(image_path)
                st.image(img, use_column_width=True)
                found_image = True

        # If no matching image with the selected color, display any random image of the class
        if not found_image:
            class_images = [img for img in all_images if img.startswith(selected_class.lower())]
            if class_images:
                random_image = random.choice(class_images)
                image_path = os.path.join('100_images', random_image)
                if os.path.exists(image_path):
                    img = Image.open(image_path)
                    st.image(img, use_column_width=True)
                    found_image = True

        # Display a message if no image was found for the selected class and color
        if not found_image:
            st.write("No matching image found.")

else:
    # File uploader for image prediction
    file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

    if file is not None:
        image = Image.open(file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        img_array = np.array(image.resize((32, 32)))
        img_array = np.expand_dims(img_array, axis=0)

        # Predict class for the uploaded image
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)
        class_name = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
        predicted_label = class_name[predicted_class]

        st.write(f"Predicted Class: {predicted_label}")

        # Display color and images based on predicted class
        selected_class = predicted_label
        filtered_data = df[df['Class'] == selected_class]

        unique_colors_for_class = filtered_data['Dominant Color'].unique()
        selected_color = st.selectbox("Select a dominant color:", ['Any'] + list(unique_colors_for_class))

        if selected_color != 'Any':
            filtered_filenames = filtered_data[filtered_data['Dominant Color'] == selected_color]['File Name']
            has_selected_color = len(filtered_filenames) > 0
        else:
            filtered_filenames = filtered_data['File Name']
            has_selected_color = True

        found_image = False
        all_images = os.listdir('100_images')

        available_images = [img for img in all_images if img in filtered_filenames.values]

        if has_selected_color and available_images:
            random_image = random.choice(available_images)
            image_path = os.path.join('100_images', random_image)
            if os.path.exists(image_path):
                img = Image.open(image_path)
                st.image(img, use_column_width=True)
                found_image = True

        if not found_image:
            class_images = [img for img in all_images if img.startswith(selected_class.lower())]
            if class_images:
                random_image = random.choice(class_images)
                image_path = os.path.join('100_images', random_image)
                if os.path.exists(image_path):
                    img = Image.open(image_path)
                    st.image(img, use_column_width=True)
                    found_image = True

        if not found_image:
            st.write("No matching image found.")
