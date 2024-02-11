# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import polars as pl

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="NARSIL",
        page_icon="❇",
        layout="wide"
    )

    st.write("# NARSIL WEAVE TERMINAL")

    # todo: change to st.columns([3,1,1]) when width is figured out
    col1, col2, col3 = st.columns(3)

    with col1:
      st.write(
          """
          ### CAPEX
          Optimally allocate incoming capital
          """
      )
      with st.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')

    with col2:
      st.write(
          """
          ### FABRICATION
          Specify and manufacture bleeding-edge designs
          """
      )
      with st.form(key='my_form2'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')

    with col3:
      st.write(
          """
          ### DEPLOYMENT
          Deploy in-theatre for kinetic effect generation
          """
      )
      with st.form(key='my_form3'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')

    st.write("## Modelled Effect on Target")
    x = st.button('ENGAGE')



if __name__ == "__main__":
    run()
