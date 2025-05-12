import streamlit as st
from PIL import Image
import os

def main():
    st.title("My First Streamlit App")
    st.header("Welcome to the App")
    st.subheader("This is a subheader")
    st.write("Streamlit makes it easy to build web apps for machine learning and data science.")

    # Image uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width =True)

        # Save the uploaded image
        save_path = os.path.join("uploaded_images", uploaded_file.name)
        os.makedirs("uploaded_images", exist_ok=True)
        image.save(save_path)

        st.success(f"Image saved at: {save_path}")

if __name__ == '__main__':
    main()
