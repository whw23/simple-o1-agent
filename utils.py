import streamlit as st
import os
import json

# 加载语言文件
def load_language(lang_code):
    try:
        with open(f"lang/{lang_code}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Load language file failed: {e}")
        return {}

# 获取语言列表
def get_language_list():
    try:
        return [f.split(".")[0] for f in os.listdir("lang") if f.endswith(".json")]
    except Exception as e:
        st.error(f"Load language list failed: {e}")
        return []