import streamlit as st
import pandas as pd


def show_detection_table(detections):

    st.subheader("Detected Defects")

    if len(detections) == 0:

        st.success("No Defects Found")

        return

    df = pd.DataFrame(detections)

    st.dataframe(
        df,
        use_container_width=True
    )