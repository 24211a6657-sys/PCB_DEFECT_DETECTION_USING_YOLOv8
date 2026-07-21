import streamlit as st


def show_images(original, detected):

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original PCB")

        st.image(
            original,
            use_container_width=True
        )

    with col2:

        st.subheader("Detection Result")

        st.image(
            detected,
            use_container_width=True
        )