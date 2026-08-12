import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show_dashboard(df):

    st.subheader("📊 Enterprise Dashboard")

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    # -----------------------------
    # Data Table
    # -----------------------------

    st.subheader("📋 Data")

    st.dataframe(
        df,
        use_container_width=True
    )

    # -----------------------------
    # Numeric Columns
    # -----------------------------

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:

        st.subheader(
            "📈 Data Visualization"
        )

        selected_column = st.selectbox(
            "Select numeric column",
            numeric_columns
        )

        fig, ax = plt.subplots()

        df[selected_column].plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            f"{selected_column} Visualization"
        )

        ax.set_xlabel("Records")

        ax.set_ylabel(
            selected_column
        )

        st.pyplot(fig)

    else:

        st.info(
            "No numeric columns available for visualization."
        )