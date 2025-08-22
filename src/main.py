import streamlit as st
from page.ai_projects import get_ai_projects_overview

st.set_page_config(page_title="AI-projekter", page_icon="assets/favicon.ico")

get_ai_projects_overview()
