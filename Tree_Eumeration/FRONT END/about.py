import streamlit as st

def run():
    st.title("About Us")
    st.write("""
       Accurate tree enumeration is essential for forest land diversion, environmental monitoring, and sustainable forestry management. 
             Traditional methods rely on manual counting, which is time-consuming, labor-intensive, and prone to errors. This paper presents an automated tree enumeration system using advanced image analytics and deep learning models, including YOLOv8, YOLOv9, YOLOv10. The system processes aerial and satellite images to detect, count, and classify trees with high accuracy.
The backend, developed in Python, integrates OpenCV and TensorFlow for image processing and real-time object detection. 
             The frontend, built using Streamlit, provides a user-friendly interface for image uploads and instant 
             visualization of tree count results. By automating tree enumeration, this system significantly improves 
             accuracy and efficiency, aiding environmental authorities, policymakers, and forest management professionals
              in making data-driven decisions for sustainable land use

    """)
    st.image("dp2.jpg", caption="About Image")
