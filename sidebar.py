import streamlit as st
import os
from sidebar_tabs.tabChathistory import render_chathistory
from sidebar_tabs.tabLLM import render_settings
from sidebar_tabs.tabSettings import render_language  # 导入语言渲染函数

def render_sidebar():
    tabChathistory,tabLLM, tabSettings = st.sidebar.tabs(
        [
            st.session_state.language_data.get("chat_tab", "💬 聊天"),
            st.session_state.language_data.get("LLM_tab", "🤖 LLM"),
            st.session_state.language_data.get("settings_tab", "🌐 语言")
        ]
    )

    with tabChathistory:
        render_chathistory()  # 调用聊天历史渲染函数

    with tabLLM:
        render_settings()  # 调用设置渲染函数

    with tabSettings:
        render_language()  # 调用语言渲染函数