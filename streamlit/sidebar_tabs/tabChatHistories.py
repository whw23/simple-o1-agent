import streamlit as st

def render_chat_histories():
    st.write(st.session_state.language_data.get("chat_history_interface", "这里是聊天记录界面"))