import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
import pandas as pd
from playsound import playsound
import matplotlib.pyplot as plt
import torch
torch.classes.__path__ = []

print("Started")

# Load the trained YOLO model
@st.cache_resource
def load_yolo_model():
    model = YOLO('best.pt')  # Adjust the model path accordingly
    print("model loaded")
    return model

# Initialize YOLO model
model = load_yolo_model()

def predict_image(image):
    results = model.predict(image, conf=0.10, iou=0.10, save=False, show=False)
    print("results:", results)
    return results

def display_results_as_dataframe(results):
    boxes = results[0].boxes
    df = pd.DataFrame(boxes.xywh.cpu().numpy(), columns=['x_center', 'y_center', 'width', 'height'])
    df['confidence'] = boxes.conf.cpu().numpy()
    df['class_id'] = boxes.cls.cpu().numpy()
    df['class_name'] = [model.names[int(cls)] for cls in df['class_id']]  # Get class names from model
    print("df:", df)
    return df

def run():
    st.title("Tree Detection")
    st.write("Upload an image to predict objects")

    # Option: Image upload for prediction
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)  # Display uploaded image

        # Convert image to numpy array for processing
        image_array = np.array(image)
        
        # Pass image to YOLO for prediction
        results = predict_image(image_array)

        # Display results
        st.write("Prediction Results:")
        prediction_df = display_results_as_dataframe(results)
        st.write(prediction_df)  # Display prediction results as pandas DataFrame

        # Show total count of detected objects
        total_count = len(prediction_df)
        st.write(f"**Total Trees Detected:** {total_count}")

        # Access the image with predictions directly from the results
        img_with_predictions = results[0].plot()

        # Display the image with predictions using matplotlib
        plt.figure(figsize=(10, 10))
        plt.imshow(cv2.cvtColor(img_with_predictions, cv2.COLOR_RGBA2RGB))  # Convert BGR to RGB for correct display
        plt.axis('off')  # Turn off axis labels
        st.pyplot(plt)

if __name__ == '__main__':
    run()
