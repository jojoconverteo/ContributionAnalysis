import pandas as pd
import streamlit as st
import plotly.express as px
import config

st.title("Contribution : Analyse Streamlit")

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])

if data is not None:
    df = pd.read_csv(data, encoding=config.encoding, sep=config.sep)
    min_cluster = min(config.cluster)
    max_cluster = max(config.cluster)
    cluster = st.slider("Cluster :", min_cluster, max_cluster)

    if cluster is not None:
        df_cluster = df.query(f"{config.column_cluster} == {cluster}").drop(
            config.column_cluster, axis=1
        )
        df_melt = pd.melt(df_cluster, id_vars=config.column_date)
        if st.checkbox("Contribution Temporel :"):
            fig = px.line(df_melt, x=config.column_date, y="value", color="variable")
            st.plotly_chart(fig)

        if st.checkbox("Contribution Moyenne :"):
            df_bar = df_melt.groupby("variable").mean().reset_index()
            fig = px.bar(
                df_bar.sort_values(by="value"), x="value", y="variable", orientation="h"
            )
            st.plotly_chart(fig)
