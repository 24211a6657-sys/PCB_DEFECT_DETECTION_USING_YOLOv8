import streamlit as st


def show_header():

    st.markdown(
        """
        <div class="main-header">
            <h1>🔬 AI-Powered PCB Inspection System</h1>
            <h3>Grid-Based Defect Localization using YOLOv8</h3>
            <p>Computer Vision | Deep Learning | Industrial Quality Inspection</p>
        </div>
        """,
        unsafe_allow_html=True
    )