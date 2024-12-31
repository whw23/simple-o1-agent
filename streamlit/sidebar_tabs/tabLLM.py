import streamlit as st
import os
import requests


def fetch_model_list(api_key, base_url, service_provider):
    # 处理 base_url 末尾是否有斜杠
    if base_url.endswith("/"):
        base_url = base_url[:-1]

    ########## OpenAI API ##########
    if service_provider == "OpenAI API":
        try:
            response = requests.get(f"{base_url}/models", headers={"Authorization": f"Bearer {api_key}"})
            if response.status_code == 200:
                models = response.json().get("data", [])
                return [model["id"] for model in models]
            else:
                st.exception(f"Status code: {response.status_code}. Response: {response.content.decode("utf-8")}")
                return []
        except requests.exceptions.RequestException as req_err:
            st.exception(f"Request failed: {req_err}")
            return []
        
    ########## Azure OpenAI ##########
    elif service_provider == "Azure OpenAI":
        try:
            response = requests.get(f"{base_url}/openai/models?api-version=2024-10-21", headers={"api-key": f"{api_key}"})
            if response.status_code == 200:
                models = response.json().get("data", [])
                return [model["id"] for model in models]
            else:
                st.exception(f"Status code: {response.status_code}. Response: {response.content.decode("utf-8")}")
                return []
        except requests.exceptions.RequestException as req_err:
            st.exception(f"Request failed: {req_err}")
            return []
    
    ########## Common ##########
    return []


def render_settings():
    service_provider = st.pills(st.session_state.language_data.get(
        "service_provider", "服务商"), options=["OpenAI API", "Azure OpenAI"],default="OpenAI API", key="service_provider")
    ########## OpenAI API ##########
    if service_provider == "OpenAI API":
        api_key = st.text_input(st.session_state.language_data.get(
            "api_key", "🔑 API Key"), value=os.getenv("API_KEY", ""), key="api_key", type="password")
        base_url = st.text_input(st.session_state.language_data.get(
            "base_url", "🔗 Base URL"), value=os.getenv("BASE_URL", "https://api.openai.com/v1"), key="base_url")
        use_selectbox = st.toggle(st.session_state.language_data.get("toggle_model_input", "切换模型输入方式"))
        if use_selectbox:
            model_list = fetch_model_list(api_key, base_url, service_provider)
            st.session_state.model_list = model_list
            model_input = st.selectbox(st.session_state.language_data.get(
                "select_model", "选择模型"), options=st.session_state.model_list, key="model_select")
        else:
            model_input = st.text_input(st.session_state.language_data.get(
                "input_model", "输入模型"), value=os.getenv("MODEL", "gpt-4o"), key="model_input")

        role_options = ["system", "developer"]
        selected_role = st.selectbox(st.session_state.language_data.get(
            "system_role", "系统角色"), options=role_options, index=role_options.index(os.getenv("ROLE", "system")), key="role_select")
        stream_output = st.checkbox(st.session_state.language_data.get("stream_output", "流式输出"), value=os.getenv("STREAM_OUTPUT", False), key="stream_output")
        
    ########## Azure OpenAI ##########
    elif service_provider == "Azure OpenAI":
        api_key = st.text_input(st.session_state.language_data.get(
            "api_key", "🔑 API Key"), value=os.getenv("API_KEY", ""), key="api_key", type="password")
        base_url = st.text_input(st.session_state.language_data.get(
            "base_url", "🔗 Base URL"), value=os.getenv("BASE_URL", "https://api.openai.com/v1"), key="base_url")
        api_version = st.text_input(st.session_state.language_data.get(
            "api_version", "API Version"), value=os.getenv("API_VERSION", "2024-10-21"), key="api_version")
        use_selectbox = st.toggle(st.session_state.language_data.get("toggle_model_input", "切换模型输入方式"))
        if use_selectbox:
            model_list = fetch_model_list(api_key, base_url, service_provider)
            st.session_state.model_list = model_list
            model_input = st.selectbox(st.session_state.language_data.get(
                "select_model", "选择模型"), options=st.session_state.model_list, key="model_select")
        else:
            model_input = st.text_input(st.session_state.language_data.get(
                "input_model", "输入模型"), value=os.getenv("MODEL", "gpt-4o"), key="model_input")

        role_options = ["system", "developer"]
        selected_role = st.selectbox(st.session_state.language_data.get(
            "system_role", "系统角色"), options=role_options, index=role_options.index(os.getenv("ROLE", "system")), key="role_select")
        stream_output = st.checkbox(st.session_state.language_data.get("stream_output", "流式输出"), value=os.getenv("STREAM_OUTPUT", False), key="stream_output")

    ########## Common ##########
    else:
        return