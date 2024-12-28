import streamlit as st
import os
from sidebar_tabs.tabChatHistories import render_chat_histories
from sidebar_tabs.tabLLM import render_settings
from sidebar_tabs.tabSettings import render_language  # 导入语言渲染函数

def render_sidebar():
    tabChatHistories, tabLLM, tabSettings = st.sidebar.tabs(
        [
            st.session_state.language_data.get("chat_tab", "💬 聊天"),
            st.session_state.language_data.get("LLM_tab", "🤖 LLM"),
            st.session_state.language_data.get("settings_tab", "🌐 语言")
        ]
    )

    with tabChatHistories:
        render_chat_histories()  # 调用聊天记录渲染函数

    with tabLLM:
        render_settings()  # 调用设置渲染函数

    with tabSettings:
        render_language()  # 调用语言渲染函数