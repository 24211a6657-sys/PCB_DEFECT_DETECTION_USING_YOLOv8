import streamlit as st


def show_metrics(health):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "PCB Health",
            f'{health["health_score"]}%'
        )

    with col2:
        st.metric(
            "Status",
            health["status"]
        )

    with col3:
        st.metric(
            "Total Defects",
            health["total_defects"]
        )