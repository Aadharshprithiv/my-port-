import streamlit as st
from PIL import Image
import datetime

st.set_page_config(page_title="Camera Sensing App", layout="centered")

st.title("📷 Camera Sensing Website")
st.write("Camera Access | Image Capture | Save Image")

# Open camera
camera_image = st.camera_input("Open Camera")

if camera_image is not None:
    # Load image using PIL
    image = Image.open(camera_image)

    st.success("✅ Image captured successfully!")

    # Display image
    st.image(image, caption="Captured Image", use_container_width=True)

    # Save image option
    if st.button("💾 Save Image"):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"captured_{timestamp}.png"
        image.save(filename)
        st.success(f"Image saved as {filename}")

st.markdown("---")
st.caption("Streamlit Camera App |  prithivi innerwears 😎")