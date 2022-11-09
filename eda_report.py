#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate TD-Brain Dataset report and deploy it via Streamlit
@author: christos
"""

# =============================================================================
# IMPORT MODULES
# =============================================================================
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling
import pandas as pd


# st.set_page_config(page_title='TD-EDA Report',
#                    page_icon=":brain:", layout='wide')
# # =============================================================================
# # LOCAL CSS
# # =============================================================================
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#         hide_streamlit_style = """
#                     <style>
#                     #MainMenu {visibility: hidden;}
#                     footer {visibility: hidden;}
#                     </style>
#                     """
#         st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# local_css("style/style.css")


tsv_fname = 'participants.tsv'
tsv_file = pd.read_csv(tsv_fname,
                       sep='\t',
                       index_col=False,
                       low_memory=False)

model_dev_subject_id = tsv_file.copy().query('indication != "REPLICATION"')
# generate profile
profile = pandas_profiling.ProfileReport(
    model_dev_subject_id, title='TD-Brain EDA')
st.title("TD-Brain EDA")

st.write(model_dev_subject_id)
st_profile_report(profile)
