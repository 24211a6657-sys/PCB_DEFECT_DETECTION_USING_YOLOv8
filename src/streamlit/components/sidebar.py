import streamlit as st


def show_sidebar():

    st.sidebar.title("⚙ Dashboard")

    uploaded_file = st.sidebar.file_uploader(
        "Upload PCB Image",
        type=["jpg", "jpeg", "png"]
    )

    confidence = st.sidebar.slider(
        "Confidence Threshold",
        0.0,
        1.0,
        0.25,
        0.05
    )

    st.sidebar.markdown("---")

    st.sidebar.subheader("📊 Model Information")

    st.sidebar.write("Model : YOLOv8n")

    st.sidebar.write("Classes : 6")

    st.sidebar.write("Dataset : PCB Defect Dataset")

    st.sidebar.write("Version : 8.4.87")

    st.sidebar.markdown("---")

    st.sidebar.info(
        "AI Powered PCB Inspection using YOLOv8"
    )

    return uploaded_file, confidence