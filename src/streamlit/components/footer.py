import streamlit as st


def show_footer():

    st.markdown("---")

    st.markdown(
        """
        <div class='footer'>
        AI Powered PCB Inspection System using YOLOv8
        <br>
        Developed for Industrial PCB Quality Inspection
        </div>
        """,
        unsafe_allow_html=True
    )