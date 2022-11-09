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

# define the root path where the raw data are stored

tsv_fname = 'participants.tsv'
tsv_file = pd.read_csv(tsv_fname,
                       sep='\t',
                       index_col=False,
                       low_memory=False)
# generate profile
profile = pandas_profiling.ProfileReport(tsv_file, title='TD-Brain EDA')
st.title("TD-Brain EDA")

st.write(tsv_file)
st_profile_report(profile)
