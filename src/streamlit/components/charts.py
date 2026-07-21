import streamlit as st
import pandas as pd


def show_chart(health):

    if len(health["summary"]) == 0:

        return

    df = pd.DataFrame(

        {

            "Defect": list(health["summary"].keys()),

            "Count": list(health["summary"].values())

        }

    )

    st.subheader("Defect Distribution")

    st.bar_chart(
        df.set_index("Defect")
    )