import streamlit as st
import os
from utils import load_language, get_language_list


def render_language():
    # 从st.session_state.language中获取当前语言
    current_language = st.session_state.language
    # 获取语言列表
    language_list = get_language_list()
    # 语言选择下拉框
    selected_language = st.selectbox(st.session_state.language_data.get(
        "language_select", "选择语言"), options=language_list, index=language_list.index(current_language), 
        key="language_select")
    # 如果选择的语言和当前语言不一致
    if selected_language != current_language:
        # 更新当前语言
        st.session_state.language = selected_language
        # 重新加载语言数据
        st.session_state.language_data = load_language(selected_language)
        # 重新加载页面
        st.rerun()
