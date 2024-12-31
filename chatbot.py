import streamlit as st
import os
from dotenv import load_dotenv
from sidebar import render_sidebar  # 导入 sidebar 模块
from utils import load_language  # 导入加载语言函数

load_dotenv()

st.set_page_config(page_title="chat", page_icon="🤔", layout="wide",
                   initial_sidebar_state="collapsed", menu_items=None)

# 初始化语言设置
if 'language' not in st.session_state:
    st.session_state.language = os.getenv("LANGUAGE", "zh-CN")
    st.session_state.language_data = load_language(st.session_state.language)

# 渲染 sidebar
render_sidebar()

st.markdown(
    """
    <style>
        .stAppHeader {
            # display: none;
        }
        .stAppDeployButton{
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)
