import streamlit as st


def show_recommendations(recommendations):

    st.subheader("Recommendations")

    for recommendation in recommendations:

        st.info(recommendation)